# 🎓 ClassPulse AI: Real-Time Lecture Analysis & Quiz Generator

![Project Status](https://img.shields.io/badge/Status-Active-success)
![Education](https://img.shields.io/badge/Focus-Education_Tech-orange)
![AI Powered](https://img.shields.io/badge/AI-Gemini_Flash-blue)

## 📖 Overview

**ClassPulse AI** helps teachers understand classroom comprehension in real time by transcribing lectures, generating AI-powered insights, and creating instant quizzes.

## ✨ Key Features

- **Live Lecture Transcription** using Web Speech API
- **AI-Powered Analysis** of lecture content
- **Instant Quiz Generation** from classroom sessions
- **Comprehension Scoring** with feedback
- **Local History Storage** for past sessions

## 💻 Tech Stack

- **Frontend:** HTML5, Vanilla JavaScript, Tailwind CSS
- **Backend:** FastAPI
- **AI Integrations:** g4f, Ollama, Hugging Face fallback pipeline
- **Speech Engine:** Web Speech API (`SpeechRecognition` / `webkitSpeechRecognition`)

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ClassPulse-AI.git
   cd ClassPulse-AI
   ```

2. **(Optional) Run backend locally**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   uvicorn ClassPulse_AI.backend.main:app --reload
   ```

3. **Run the app**
   - Backend mode: open `http://127.0.0.1:8000`
   - Static mode: open `ClassPulse_AI/ui/index.html` directly in a supported browser

## 🔐 Environment Variables

> Current frontend configuration uses a JavaScript constant for API key entry. For secure deployment, inject secrets from environment variables on the server/build side and do not commit keys.

| Variable | Required | Purpose |
|---|---|---|
| `GEMINI_API_KEY` | Recommended | Google Gemini API key for AI calls (inject at runtime/build; never commit). |
| `HF_TOKEN` or `HUGGINGFACEHUB_API_TOKEN` | Optional | Auth token for Hugging Face Inference when required. |
| `OLLAMA_HOST` | Optional | Custom Ollama host endpoint for local/remote model execution. |

## 🧩 Troubleshooting

- **Microphone not working**
  - Allow mic permissions in browser settings.
  - Use HTTPS or localhost for speech APIs.
- **AI generation fails**
  - Verify API keys/tokens are valid and not rate-limited.
  - Check network access for provider endpoints.
- **UI not loading from backend**
  - Confirm `uvicorn ClassPulse_AI.backend.main:app --reload` is running.
- **Slow responses**
  - Reduce transcript size and retry.
  - Prefer local Ollama or valid provider credentials for faster responses.

## 🌐 Browser Compatibility

- **Recommended:** Latest Chrome or Edge (best support for speech recognition APIs)
- **Partial/limited support:** Firefox, Safari (speech recognition behavior may vary)
- Always test microphone and speech recognition features on your target browser/device.

## ⚡ Performance Considerations

- Keep transcript input concise when possible to reduce AI latency.
- The backend truncates large transcripts before prompt generation for faster inference.
- Use local AI backends (e.g., Ollama) when low-latency processing is required.
- Stable internet and low browser extension overhead improve real-time transcription quality.

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for setup, style, testing, and PR guidelines.

## 🛡️ Security

Please read [SECURITY.md](SECURITY.md) for API key handling, secure credential practices, and vulnerability reporting.

## 📝 License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
