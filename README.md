# 🎓 ClassPulse AI: Real-Time Lecture Analysis & Quiz Generator

![Project Status](https://img.shields.io/badge/Status-Active-success)
![Education](https://img.shields.io/badge/Focus-Education_Tech-orange)
![AI Powered](https://img.shields.io/badge/AI-Gemini_Flash-blue)

## 📖 Overview

**ClassPulse AI** is an intelligent classroom assistant designed to bridge the gap between teaching and student comprehension.

In a traditional classroom, it can be difficult for teachers to gauge if students are actively listening and understanding the material in real-time. This project solves that problem by:
1. **Transcribing** the teacher's lecture live into text.
2. **Analyzing** lecture content with AI.
3. **Generating** instant quiz questions from the session.

This enables immediate in-class assessment and helps identify knowledge gaps quickly.

## ✨ Key Features

### 🎙️ For the Classroom
- **Live Lecture Transcription:** Captures speech in real-time using Web Speech API.
- **Multi-Language Support:** Works with multiple languages (English, Hindi, Telugu, etc.).
- **Distraction-Free Interface:** Clean UI for classroom use.

### 🧠 AI-Powered Assessment
- **Instant Quiz Generation:** Creates multiple-choice quiz questions from lecture content.
- **Comprehension Scoring:** Checks answers and provides a score.
- **Executive Summaries:** Produces concise notes and takeaways.

### 🛠 Technical Highlights
- **Voice-to-Text:** Continuous recognition with retry behavior.
- **Local Storage:** Saves class history in-browser.
- **Dark Mode:** Improved visibility during classroom presentations.

---

## 🚀 How It Works in Class

1. Start the session and click the **Microphone** button.
2. Teach normally while ClassPulse transcribes the lecture.
3. Click **AI Insights** to analyze the transcript.
4. Use generated quiz content for quick assessment.

---

## 💻 Tech Stack

- **Frontend:** HTML5, JavaScript (Vanilla)
- **Styling:** Tailwind CSS
- **Backend:** FastAPI (`ClassPulse_AI/backend/main.py`)
- **AI/LLM Integration:** Multi-provider fallback in backend
- **Speech Engine:** Web Speech API (`webkitSpeechRecognition`)

---

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ClassPulse-AI.git
   cd ClassPulse-AI
   ```

2. **Run frontend only**
   - Open `ClassPulse_AI/ui/index.html` in a supported browser.

3. **Run backend (recommended)**
   ```bash
   uvicorn ClassPulse_AI.backend.main:app --reload
   ```
   Then open `http://127.0.0.1:8000`.

---

## 🔐 Environment Variable Setup

For secure deployments, use environment variables instead of hardcoded credentials.

1. Create a local `.env` file (do not commit it):
   ```bash
   cp .env.example .env
   ```
   If `.env.example` is not present yet, create `.env` manually.

2. Add your secrets to `.env`:
   ```env
   GEMINI_API_KEY=your_key_here
   HUGGINGFACEHUB_API_TOKEN=your_token_here
   ```

3. Load `.env` values in your runtime/deployment configuration.

> ⚠️ Do not store real API keys in `README.md`, JavaScript source, issues, or pull requests.

## 🔑 API Key Configuration Best Practices

- Use separate API keys for local development and production.
- Restrict API keys by service, quota, and allowed origins where possible.
- Rotate keys periodically and immediately after suspected exposure.
- Keep keys in secret managers for production (not in code).

## 🛡️ Security Warning

**Never commit secrets.** If an API key or credential is exposed:
1. Revoke the compromised key immediately.
2. Create a new key.
3. Update all environments with the new value.
4. Remove exposed secrets from repository history if needed.

See [`SECURITY.md`](SECURITY.md) for the full policy.

---

## 🌐 Browser Requirements

For best compatibility with speech recognition and microphone features:
- Google Chrome (latest)
- Microsoft Edge (latest)

Also ensure:
- Microphone permissions are granted.
- HTTPS or localhost context is used when required by browser policy.

## Known Limitations

- Speech recognition quality depends on microphone quality and background noise.
- Browser speech APIs may behave differently across devices and locales.
- AI-generated content may contain inaccuracies and should be reviewed before classroom use.
- Offline usage is limited for AI-backed analysis features.

## 🧰 Troubleshooting

### Microphone not working
- Confirm browser microphone permission is enabled.
- Check OS-level input device settings.
- Refresh the page after changing permissions.

### AI analysis fails or times out
- Ensure backend is running if using API routes.
- Verify network connectivity.
- Confirm required API credentials are configured in environment variables.

### Empty or poor transcript quality
- Reduce background noise.
- Speak clearly and at a moderate pace.
- Try a different microphone or browser.

---

## 🤝 Contributing

Contributions are welcome. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before submitting issues or pull requests.

## 📝 License

This project is licensed under the [MIT License](LICENSE).
