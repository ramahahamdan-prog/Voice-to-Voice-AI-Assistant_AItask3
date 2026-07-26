
# Voice-to-Voice AI Assistant

## Overview

The Voice-to-Voice AI Assistant is a Python-based application that allows users to communicate with an AI assistant using voice. The system captures the user's speech, converts it into text, sends the text to a Large Language Model (LLM) to generate an intelligent response, and finally converts the generated response back into speech.

This project demonstrates the integration of Speech Recognition, Artificial Intelligence, and Text-to-Speech technologies into a single application.

---

## Features

- Capture voice input using a microphone.
- Convert speech into text.
-  Generate AI responses using the Cohere Large Language Model.
-  Convert AI-generated text into speech.
-  Interactive voice conversation.
-  Continuous conversation until the user exits the program.

---

## Technologies Used

- **Python 3.11**
- **SpeechRecognition** – Speech-to-Text conversion
- **PyAudio** – Microphone input
- **Cohere API** – AI response generation
- **gTTS (Google Text-to-Speech)** – Text-to-Speech conversion
- **playsound** – Audio playback
- **python-dotenv** – Secure API key management

---

## Project Structure

```
Voice-AI-Assistant/
│
├── main.py
├── assistant.py
├── speech_to_text.py
├── text_to_speech.py
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How It Works

The assistant performs the following workflow:

1. The user speaks into the microphone.
2. The Speech Recognition module converts the speech into text.
3. The text is sent to the Cohere Large Language Model.
4. Cohere generates an appropriate response.
5. The response text is converted into speech using Google Text-to-Speech.
6. The generated audio is played back to the user.

### Workflow Diagram

```
User Speech
      │
      ▼
Speech-to-Text
      │
      ▼
Text
      │
      ▼
Cohere AI
      │
      ▼
AI Response
      │
      ▼
Text-to-Speech
      │
      ▼
Voice Output
```

---

## Installation

1. Clone the repository.

```bash
git clone https://github.com/yourusername/Voice-AI-Assistant.git
```

2. Navigate to the project folder.

```bash
cd Voice-AI-Assistant
```

3. Install the required packages.

```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your Cohere API key.

```text
COHERE_API_KEY=YOUR_API_KEY
```

5. Run the application.

```bash
python main.py
```

---

## Challenges

During the development of this project, several challenges were encountered:

- Installing **PyAudio** on newer Python versions (3.13 and 3.14) caused compatibility issues.
- Managing the Cohere API key securely using environment variables.
- Handling microphone permissions and speech recognition errors.
- Ensuring reliable communication between Speech-to-Text, the AI model, and Text-to-Speech.

---

## Fixes

The following solutions were applied to resolve the encountered issues:

- Created a dedicated **Conda environment** with **Python 3.11** to ensure compatibility with PyAudio.
- Stored the Cohere API key inside a `.env` file instead of hardcoding it.
- Used the `python-dotenv` package to securely load environment variables.
- Added error handling for speech recognition failures and invalid user input.

---

## Future Improvements

Possible enhancements for future versions include:

- Support for multiple languages.
- Wake-word detection (e.g., "Hey Assistant").
- Conversation history and memory.
- Voice customization (male/female voices).
- Graphical User Interface (GUI).
- Offline Speech-to-Text and Text-to-Speech support.
- Integration with additional AI models such as OpenAI or Gemini.

---

## Requirements

```
SpeechRecognition
PyAudio
cohere
gTTS
playsound==1.2.2
python-dotenv
```

---
