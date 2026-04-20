# 🎓 ClassPulse AI: Real-Time Lecture Analysis & Quiz Generator

![Project Status](https://img.shields.io/badge/Status-Active-success)
![Education](https://img.shields.io/badge/Focus-Education_Tech-orange)
![AI Powered](https://img.shields.io/badge/AI-Gemini_Flash-blue)

## 📖 Overview

**ClassPulse AI** is an intelligent classroom assistant designed to bridge the gap between teaching and student comprehension. 

In a traditional classroom, it can be difficult for teachers to gauge if students are actively listening and understanding the material in real-time. This project solves that problem by:
1.  **Transcribing** the teacher's lecture live into text.
2.  **Analyzing** the lecture content using Artificial Intelligence.
3.  **Generating** an instant, 10-question quiz based on that specific session.

This allows teachers to conduct immediate assessments at the end of a class to verify student attentiveness and identify knowledge gaps.

## ✨ Key Features

### 🎙️ For the Classroom
* **Live Lecture Transcription:** Captures the teacher's speech in real-time using the Web Speech API.
* **Multi-Language Support:** Works for various languages (English, Hindi, Telugu, etc.), making it inclusive for different regions.
* **Distraction-Free Interface:** Clean UI to display the lecture notes as they are spoken.

### 🧠 AI-Powered Assessment (Gemini Integrated)
* **Instant Quiz Generation:** With one click, the system analyzes the entire lecture and creates a **10-question multiple-choice quiz**.
* **Comprehension Scoring:** Automatically checks answers and provides a score to measure understanding.
* **Executive Summaries:** Generates a concise summary of the lecture and "Action Items" (homework or key takeaways).

### 🛠 Technical Highlights
* **Voice-to-Text:** Continuous speech recognition with auto-restart logic to ensure no part of the lecture is missed.
* **Local Storage:** Saves lecture history locally in the browser, allowing students/teachers to review past classes.
* **Dark Mode:** Classroom-friendly dark mode to reduce eye strain during presentations.

---

## 🚀 How It Works in Class

1.  **Start Class:** The teacher (or student) opens the app and clicks the **Microphone** button.
2.  **Teach:** The app listens to the lecture and types it out on the screen in real-time.
3.  **Analyze:** When the topic is finished, click the **Magic Wand (AI Insights)** button.
4.  **Quiz:** The AI generates a quiz. The teacher can project these questions to the class or have students take them individually to see who was listening!

---

## 💻 Tech Stack

* **Frontend:** HTML5, JavaScript (Vanilla)
* **Styling:** Tailwind CSS
* **AI Engine:** Google Gemini 2.5 Flash Preview (via API)
* **Speech Engine:** Web Speech API (`webkitSpeechRecognition`)

---

## ⚙️ Setup & Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/classpulse-ai.git](https://github.com/your-username/classpulse-ai.git)
    ```

2.  **Set up environment variables (recommended and secure):**
    ```bash
    cp .env.example .env
    ```
    Then update `.env` with your own values, such as:
    ```env
    GEMINI_API_KEY=your_gemini_api_key_here
    HF_TOKEN=your_huggingface_token_here
    ```

3.  **Run locally (FastAPI backend + UI):**
    ```bash
    uvicorn ClassPulse_AI.backend.main:app --reload
    ```
    Open `http://127.0.0.1:8000` in Chrome or Edge and allow microphone access.

## 🔐 Environment & Security Notes

- Never hardcode API keys directly in source files.
- Never commit `.env` files or secrets to Git.
- If a key is exposed, rotate/revoke it immediately.
- See [SECURITY.md](SECURITY.md) for full project security guidance.


## 🤝 Contribution

This project is open for enhancements! Please review [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. We welcome ideas such as:
* Exporting quiz results to PDF.
* Student login systems.
* Cloud database integration.

## 📝 License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
