
import os
import time
from gtts import gTTS
from playsound import playsound

def speak(text):
    if not text or not text.strip():
        return

    # Dynamic filename prevents Windows permission/file-locking crashes
    filename = f"speech_{int(time.time() * 1000)}.mp3"

    try:
        tts = gTTS(text=text, lang="en")
        tts.save(filename)
        playsound(filename)
    except Exception as e:
        print(f"TTS Error: {e}")
    finally:
        # Clean up audio file after playing
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except OSError:
                pass