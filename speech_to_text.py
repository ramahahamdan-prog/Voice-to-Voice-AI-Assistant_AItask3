
import speech_recognition as sr
import whisper
import numpy as np

print("Loading local Whisper model...")
# "base" or "tiny" loads fast and works well
model = whisper.load_model("base")

recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            return ""

    try:
        print("Recognizing locally...")

        # Convert raw audio bytes directly into a float32 NumPy array for Whisper
        raw_data = audio.get_raw_data(convert_rate=16000, convert_width=2)
        audio_np = np.frombuffer(raw_data, dtype=np.int16).astype(np.float32) / 32768.0

        # Transcribe directly from memory array
        result = model.transcribe(audio_np, fp16=False)
        text = result["text"].strip()

        print("You:", text)
        return text

    except Exception as e:
        print(f"Recognition Error: {e}")
        return ""