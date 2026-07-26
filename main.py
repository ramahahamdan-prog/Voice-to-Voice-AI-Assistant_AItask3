# This is a sample Python script.

from speech_to_text import listen
from assistant import ask_ai
from text_to_speech import speak

print("Voice AI Assistant Started")

while True:
    text = listen()

    if text == "":
        continue

    if text.lower() in ["exit", "quit", "stop"]:
        print("Goodbye!")
        speak("Goodbye!")
        break

    # Get answer from Cohere
    response = ask_ai(text)

    # Print the text
    print("Assistant:", response)

    # Speak the answer out loud!
    speak(response)
