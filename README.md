# 🧠 Advanced Jarvis - AI Desktop Assistant

An advanced AI-powered desktop voice assistant built with Python. Jarvis is capable of performing a variety of system tasks, answering questions, opening applications, web browsing, and much more using natural language commands.

## 🚀 Features

- 🎙️ Voice command recognition
- 🗣️ Text-to-speech (TTS) response
- 🌐 Web search (Google, Wikipedia, YouTube, etc.)
- 📧 Send emails and read inbox
- 📅 Tell time, date, and weather
- 🔒 Lock, shutdown, restart system
- 📁 Open files, folders, and applications
- 🔗 Internet speed check, screenshot capture, and more

## 🧰 Technologies Used

- Python 3
- `speech_recognition`
- `pyttsx3`
- `pywhatkit`, `wikipedia`, `pyjokes`
- `webbrowser`, `os`, `datetime`, `smtplib`
- `pyaudio` (for microphone access)

## ⚙️ Installation

### Prerequisites

- Python 3.7 or higher
- Microphone
- Internet connection (for web tasks)

### Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure you have `PyAudio` installed. If it fails via pip, install using:

```bash
pip install pipwin
pipwin install pyaudio
```

## ▶️ Run Jarvis

```bash
python jarvis.py
```

Jarvis will greet you and wait for your voice commands.

## 🗒️ Example Commands

- "Open YouTube"
- "Search for Python tutorials"
- "Send email to [contact]"
- "What is the time?"
- "Tell me a joke"
- "Lock the system"

## 🧩 File Structure

```
advanced_jarvis/
├── jarvis.py             # Main script
├── requirements.txt      # Required Python packages
├── README.md             # Project documentation
└── assets/               # (Optional) Icons, sounds, etc.
```

## ⚠️ Disclaimer

This project is created for educational purposes. Use responsibly and ensure you have the proper system permissions.

## 🙋‍♂️ Author

**Suri Puri**  
[GitHub Profile](https://github.com/suri9515)

---

Feel free to ⭐ this project if you find it helpful!
