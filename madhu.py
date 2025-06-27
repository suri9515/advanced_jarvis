import openai
from modules.voice_engine import speak

openai.api_key = "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"

def ask_gpt(query):
    try:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}]
        )
        reply = res['choices'][0]['message']['content']
        speak(reply)
    except Exception as e:
        speak("I don't understand.")
