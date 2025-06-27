import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', pyttsx3.init().getProperty('voices')[1].id)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()
