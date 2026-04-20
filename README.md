# 🎓 ClassPulse AI: Real-Time Lecture Analysis & Quiz Generator

![Project Status](https://img.shields.io/badge/Status-Active-success)
![Education](https://img.shields.io/badge/Focus-Education_Tech-orange)
![AI Powered](https://img.shields.io/badge/AI-Gemini_Flash-blue)

## 📖 Overview

**ClassPulse AI** is an intelligent classroom assistant designed to bridge the gap between teaching and student comprehension.

In a traditional classroom, it can be difficult for teachers to gauge if students are actively listening and understanding the material in real-time. This project solves that problem by:
1. **Transcribing** the teacher's lecture live into text.
2. **Analyzing** the lecture content using Artificial Intelligence.
3. **Generating** an instant, 10-question quiz based on that specific session.

This allows teachers to conduct immediate assessments at the end of a class to verify student attentiveness and identify knowledge gaps.

## ✨ Key Features

### 🎙️ For the Classroom
- **Live Lecture Transcription:** Captures the teacher's speech in real-time using the Web Speech API.
- **Multi-Language Support:** Works for various languages (English, Hindi, Telugu, etc.), making it inclusive for different regions.
- **Distraction-Free Interface:** Clean UI to display the lecture notes as they are spoken.

### 🧠 AI-Powered Assessment (Gemini Integrated)
- **Instant Quiz Generation:** With one click, the system analyzes the entire lecture and creates a **10-question multiple-choice quiz**.
- **Comprehension Scoring:** Automatically checks answers and provides a score to measure understanding.
- **Executive Summaries:** Generates a concise summary of the lecture and action items.

### 🛠 Technical Highlights
- **Voice-to-Text:** Continuous speech recognition with auto-restart logic.
- **Local Storage:** Saves lecture history locally in the browser.
- **Dark Mode:** Classroom-friendly dark mode.

---

## 💻 Tech Stack

- **Frontend:** HTML5, JavaScript (Vanilla)
- **Styling:** Tailwind CSS
- **AI Engine:** Google Gemini 2.5 Flash Preview (via API)
- **Speech Engine:** Web Speech API (`webkitSpeechRecognition`)

---

## 🚀 Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MOTURUUTTEJ/ClassPulse-AI.git
   cd ClassPulse-AI
   ```

2. **Configure API key (local dev)**
   - Open `ClassPulse_AI/ui/index.html`.
   - Find `const API_KEY = "YOUR_OWN_GEMINI_KEY";`
   - Replace with your own key for local testing only.

3. **Run the app**
   - Open `ClassPulse_AI/ui/index.html` in Chrome/Edge.
   - Allow microphone access when prompted.

---

## 🔐 Environment variables & secret management

> Current code path uses a local JavaScript constant for API key during local testing. For shared/staging/production environments, move key handling to server-side environment variables before deployment.

| Variable | Required | Purpose |
|---|---|---|
| `GEMINI_API_KEY` | Recommended for production | Store the Gemini API key outside source code (server-side). |

### API key security best practices

- Never commit keys to Git history or screenshots.
- Keep secrets in local `.env` files or deployment secret stores.
- Rotate keys immediately if exposure is suspected.
- Restrict keys in provider settings (allowed origins, usage limits, quotas).
- Prefer backend-proxy architecture so browser clients do not directly hold long-lived secrets.

See `SECURITY.md` for responsible disclosure and additional guidance.

---

## 🧪 Troubleshooting

- **Microphone not working**
  - Use Chrome/Edge.
  - Check browser permission for microphone access.
  - Ensure the page is focused and not blocked by system privacy settings.

- **AI response fails / empty output**
  - Verify your Gemini key is valid and has quota.
  - Check network connectivity.
  - Confirm key was inserted in the expected location for local testing.

- **UI loads but styles/scripts seem broken**
  - Hard refresh the browser (`Ctrl/Cmd + Shift + R`).
  - Ensure internet access is available for external CDN assets.

---

## 🎬 Demo & screenshots

- Demo videos:
  - [Class demo 1](ClassPulse_AI/ui/video_5a90712997d64b85b442f541f546bcb1.mp4)
  - [Class demo 2](ClassPulse_AI/ui/video_9a1a08dcaa3d4f559d01ee9d8e546f5b.mp4)
  - [Class demo 3](ClassPulse_AI/ui/video_ac1e4683cea94d46910e5a840d1b2ce7.mp4)

- UI screenshot:
  - ![ClassPulse AI UI](docs/images/classpulse-ui.png)

---

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening issues or pull requests.

## 🛡 Security

Please read [SECURITY.md](SECURITY.md) for vulnerability reporting and secure key handling guidance.

## 📝 License

This project is licensed under the [MIT License](LICENSE).
