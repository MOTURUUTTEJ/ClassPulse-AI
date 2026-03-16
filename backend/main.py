import os
import json
import re
import asyncio
from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import nest_asyncio

nest_asyncio.apply()

# -----------------------------
# PATH SETUP
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_DIR = os.path.join(BASE_DIR, "..", "ui")
if not os.path.exists(UI_DIR):
    UI_DIR = BASE_DIR

# -----------------------------
# FASTAPI APP
# -----------------------------
app = FastAPI(title="ClassPulse AI Backend")
app.mount("/static", StaticFiles(directory=UI_DIR), name="static")

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    index_path = os.path.join(UI_DIR, "index.html")
    if not os.path.exists(index_path):
        return HTMLResponse("<h1>index.html not found.</h1>", status_code=404)
    return open(index_path, encoding="utf-8").read()

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return Response(status_code=204)

# -----------------------------
# LAZY IMPORTS (speeds up startup)
# -----------------------------
_ollama = None
_hf_client = None
_ddgs_class = None
_boto3 = None
_g4f_client = None

def get_g4f():
    global _g4f_client
    if _g4f_client is None:
        try:
            from g4f.client import Client as G4fClient
            _g4f_client = G4fClient()
        except ImportError:
            pass
    return _g4f_client

def get_ollama():
    global _ollama
    if _ollama is None:
        try:
            import ollama as _ol
            _ollama = _ol
        except ImportError:
            pass
    return _ollama

def get_hf_client():
    global _hf_client
    if _hf_client is None:
        try:
            from huggingface_hub import InferenceClient
            _hf_client = InferenceClient()
        except ImportError:
            pass
    return _hf_client

def get_ddgs():
    global _ddgs_class
    if _ddgs_class is None:
        try:
            from duckduckgo_search import DDGS
            _ddgs_class = DDGS
        except ImportError:
            pass
    return _ddgs_class

# Model config
LOCAL_OLLAMA_MODEL = "llama3"
# Faster, smaller HF models for quick responses
HF_FAST_MODELS = [
    "mistralai/Mistral-7B-Instruct-v0.3",   # Smaller + faster than Mixtral
    "HuggingFaceH4/zephyr-7b-beta",          # Good at instruction following
    "microsoft/Phi-3-mini-4k-instruct",       # Very fast, small
]

# -----------------------------
# HELPERS
# -----------------------------
def smart_truncate(text: str, max_chars: int = 4000) -> str:
    """Keep the most informative portion of text for fast prompting."""
    text = text.strip()
    if len(text) <= max_chars:
        return text
    # Take first 60% + last 40% to capture intro and conclusion
    head = int(max_chars * 0.6)
    tail = int(max_chars * 0.4)
    return text[:head] + "\n\n[...]\n\n" + text[-tail:]

def clean_json_response(text: str) -> str:
    """Extract valid JSON from model output, handling markdown code fences."""
    text = text.strip()
    # Strip ```json ... ``` fences
    fence = re.search(r'```(?:json)?\s*([\s\S]*?)```', text)
    if fence:
        text = fence.group(1).strip()
    
    start_obj = text.find("{")
    end_obj = text.rfind("}")
    start_arr = text.find("[")
    end_arr = text.rfind("]")
    
    valid_obj = start_obj != -1 and end_obj != -1 and end_obj > start_obj
    valid_arr = start_arr != -1 and end_arr != -1 and end_arr > start_arr
    
    if valid_obj and valid_arr:
        if start_obj < start_arr:
            text = text[start_obj:end_obj + 1]
        else:
            text = text[start_arr:end_arr + 1]
    elif valid_obj:
        text = text[start_obj:end_obj + 1]
    elif valid_arr:
        text = text[start_arr:end_arr + 1]
        
    return text.strip()

async def fetch_web_context(query: str, timeout: float = 3.0) -> str:
    """Fetch DuckDuckGo context with a hard timeout. Returns '' if slow/fails."""
    def _search():
        DDGS = get_ddgs()
        if not DDGS:
            return ""
        try:
            results = DDGS().text(query, max_results=2)
            if results:
                snippets = [f"- {r['title']}: {r['body'][:200]}" for r in results]
                return "\n".join(snippets)
        except Exception:
            pass
        return ""

    try:
        loop = asyncio.get_event_loop()
        result = await asyncio.wait_for(
            loop.run_in_executor(None, _search),
            timeout=timeout
        )
        return result
    except (asyncio.TimeoutError, Exception):
        print("Web search skipped (timeout/error)")
        return ""

async def try_g4f(prompt: str, timeout: float = 30.0) -> str | None:
    """Call g4f (GPT4Free) which routes to fast, free cloud providers reliably."""
    client = get_g4f()
    if not client:
        return None
    try:
        def _call():
            response = client.chat.completions.create(
                model="gpt-4", # Known to resolve reliably in g4f 7.x
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content

        loop = asyncio.get_event_loop()
        result = await asyncio.wait_for(
            loop.run_in_executor(None, _call),
            timeout=timeout
        )
        if result and result.strip():
            print("g4f generated successfully.")
            return result
    except Exception as e:
        print(f"g4f failed: {e}")
    return None

async def try_ollama(prompt: str, timeout: float = 25.0) -> str | None:
    """Call local Ollama with a timeout. Returns None on failure."""
    ol = get_ollama()
    if not ol:
        return None
    try:
        client = ol.AsyncClient()
        response = await asyncio.wait_for(
            client.chat(
                model=LOCAL_OLLAMA_MODEL,
                messages=[{"role": "user", "content": prompt}],
                options={"num_predict": 1500, "temperature": 0.3}
            ),
            timeout=timeout
        )
        return response["message"]["content"]
    except Exception as e:
        print(f"Ollama failed: {e}")
        return None

async def try_huggingface(prompt: str, timeout: float = 45.0) -> str | None:
    """Call HuggingFace Inference API with timeout, trying fast models in order."""
    client = get_hf_client()
    if not client:
        return None

    def _call(model: str) -> str:
        return client.text_generation(
            prompt,
            model=model,
            max_new_tokens=1200,   # Reduced from 2048 for speed
            temperature=0.3,       # Lower = faster, more deterministic
            return_full_text=False,
            do_sample=False,       # Greedy decoding = faster
        )

    for model in HF_FAST_MODELS:
        try:
            print(f"Trying HuggingFace model: {model}")
            loop = asyncio.get_event_loop()
            result = await asyncio.wait_for(
                loop.run_in_executor(None, _call, model),
                timeout=timeout
            )
            if result and result.strip():
                print(f"HuggingFace success with {model}")
                return result
        except asyncio.TimeoutError:
            print(f"HuggingFace timeout on {model}, trying next...")
        except Exception as e:
            print(f"HuggingFace error on {model}: {e}")

    return None

async def generate_with_fallback(prompt: str) -> str:
    """
    Fast generation pipeline:
    1. Try g4f (GPT4Free) for instant remote cloud processing
    2. Try local Ollama (25s timeout)
    3. Try HuggingFace fast models (45s timeout each)
    """
    # 1. Try g4f first as it is extremely fast and doesn't require local GPU compute
    result = await try_g4f(prompt, timeout=30.0)
    if result:
        return result

    # 2. Try Ollama next (fast if running locally)
    result = await try_ollama(prompt, timeout=25.0)
    if result:
        return result

    # 3. Fall back to HuggingFace
    result = await try_huggingface(prompt, timeout=45.0)
    if result:
        return result

    raise Exception(
        "All AI backends failed. "
        "Tip: Run 'pip install -U g4f' to fix the free endpoint."
    )

# -----------------------------
# PROMPT BUILDER
# -----------------------------
def build_analysis_prompt(text: str, web_context: str) -> str:
    ctx_block = f"\n\nExtra context:\n{web_context}" if web_context.strip() else ""
    return f"""You are an expert educational AI. Analyze the lecture below and return ONLY a valid JSON object.

JSON structure (no extra text, no markdown fences):
{{
  "notes": "<markdown study guide with sections: ## Summary, ## Key Concepts, ## Details>",
  "teacher_score": {{
    "score": <1-10>,
    "simplicity": <1-10>,
    "clarity": <1-10>,
    "examples": <1-10>,
    "feedback": "<one paragraph of actionable feedback>"
  }},
  "flashcards": [
    {{"term": "<term>", "definition": "<definition>"}},
    ... (5-8 cards)
  ],
  "quiz": [
    {{
      "id": "1",
      "question": "<question>",
      "options": [
        {{"text": "<correct answer>", "type": "correct"}},
        {{"text": "<wrong>", "type": "distractor"}},
        {{"text": "<plausible wrong>", "type": "distractor"}},
        {{"text": "<common misconception>", "type": "misconception"}}
      ],
      "correctAnswer": "<correct answer text>",
      "concept": "<topic name>",
      "isRemediation": false,
      "explanation": "<why the correct answer is right>"
    }},
    ... (5-8 questions)
  ]
}}

Lecture:
{text}{ctx_block}

IMPORTANT: Output ONLY the JSON object. No preamble, no explanation."""

# -----------------------------
# REQUEST MODELS
# -----------------------------
class TranscriptRequest(BaseModel):
    text: str

class VideoRequest(BaseModel):
    text: str

# -----------------------------
# API ENDPOINTS
# -----------------------------
@app.post("/api/generate-notes")
async def generate_notes(data: TranscriptRequest):
    if not data.text.strip():
        raise HTTPException(status_code=400, detail="Empty transcript")

    # Truncate text smartly to keep prompt short → faster inference
    truncated = smart_truncate(data.text, max_chars=4000)

    # Run web search in PARALLEL with prompt construction (non-blocking, 3s max)
    query = " ".join(data.text.split()[:12])
    web_task = asyncio.create_task(fetch_web_context(query, timeout=3.0))

    # Build prompt (instant)
    # We await the web search now — it either finished or timed out
    web_context = await web_task

    prompt = build_analysis_prompt(truncated, web_context)

    try:
        raw = await generate_with_fallback(prompt)
        cleaned = clean_json_response(raw)
        result = json.loads(cleaned)
        return result
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}\nRaw output:\n{raw[:500]}")
        return JSONResponse(
            status_code=500,
            content={"error": "AI returned malformed JSON. Please try again."}
        )
    except Exception as e:
        print(f"Generation failed: {e}")
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

# -----------------------------
# VIDEO GENERATION
# -----------------------------
@app.post("/api/generate-video")
async def generate_video_endpoint(data: VideoRequest):
    if not data.text.strip():
        raise HTTPException(status_code=400, detail="Empty text for video")

    try:
        import edge_tts
        from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
        from PIL import Image, ImageDraw, ImageFont
        import textwrap
        import uuid

        script_prompt = f"""Turn this into a 4-scene video lecture script.
Return ONLY a JSON array:
[{{"text": "<narration 2-3 sentences>", "visual": "<slide title>"}}]

Content: {data.text[:2000]}"""

        raw = await generate_with_fallback(script_prompt)
        # Stronger regex JSON array extractor
        match = re.search(r'\[\s*\{.*?\}\s*\]', raw, re.DOTALL)
        if match:
            cleaned = match.group(0)
        else:
            cleaned = clean_json_response(raw)

        try:
            script = json.loads(cleaned)
            # Ensure it's a list even if model messed up
            if isinstance(script, dict):
                script = [script]
        except Exception as json_err:
            print(f"Video JSON error: {json_err}. Raw:\n{raw}")
            raise Exception("AI failed to output a valid JSON list for the video script.")

        clips = []
        temp_files = []
        output_filename = f"video_{uuid.uuid4().hex}.mp4"
        output_path = os.path.join(UI_DIR, output_filename)
        W, H = 1920, 1080

        try:
            font = ImageFont.truetype("arial.ttf", 60)
            title_font = ImageFont.truetype("arialbd.ttf", 90)
        except Exception:
            font = ImageFont.load_default()
            title_font = ImageFont.load_default()

        VOICE = "en-US-AriaNeural"

        for i, scene in enumerate(script):
            audio_path = os.path.join(BASE_DIR, f"temp_audio_{i}.mp3")
            communicate = edge_tts.Communicate(scene["text"], VOICE)
            await communicate.save(audio_path)
            temp_files.append(audio_path)

            audio_clip = AudioFileClip(audio_path)
            duration = audio_clip.duration + 0.5

            img = Image.new('RGB', (W, H), color=(15, 23, 42))
            d = ImageDraw.Draw(img)
            d.text((W/2, H/3), scene["visual"].upper(), font=title_font, fill=(99, 102, 241), anchor="mm")

            margin = 100
            lines = textwrap.wrap(scene["text"], width=(W - 2*margin) // 35)
            y_text = (H * 2/3) - (len(lines) * 80 / 2)
            for line in lines:
                d.text((W/2, y_text), line, font=font, fill=(248, 250, 252), anchor="mm")
                y_text += 80

            img_path = os.path.join(BASE_DIR, f"temp_img_{i}.png")
            img.save(img_path)
            temp_files.append(img_path)

            video_clip = ImageClip(img_path).set_duration(duration).set_audio(audio_clip)
            clips.append(video_clip)

        final_video = concatenate_videoclips(clips)
        final_video.write_videofile(
            output_path, fps=24, codec="libx264",
            audio_codec="aac", preset="ultrafast"   # ultrafast encoding
        )

        for f in temp_files:
            if os.path.exists(f):
                os.remove(f)

        # Try S3 upload (optional, graceful skip if not configured)
        try:
            import boto3
            s3 = boto3.client('s3')
            bucket = "classpulse-media-906615255505"
            s3.upload_file(output_path, bucket, output_filename)
            url = s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': bucket, 'Key': output_filename},
                ExpiresIn=3600
            )
            if os.path.exists(output_path):
                os.remove(output_path)
            return {"video_url": url}
        except Exception as s3_err:
            print(f"S3 upload skipped: {s3_err}")
            return {"video_url": f"/static/{output_filename}"}

    except Exception as e:
        print(f"Video generation failed: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
