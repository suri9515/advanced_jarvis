import datetime
import pywhatkit
import wikipedia
import pyjokes
import os
import webbrowser
import pyautogui
import smtplib
import time
from email.message import EmailMessage
from modules.voice_engine import speak
from modules.weather import get_weather
from modules.madhu import ask_gpt


def send_email(to_email, subject, body):
    try:
        email = "your_email@gmail.com"
        password = "your_app_password"
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email
        msg['To'] = to_email
        msg.set_content(body)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(email, password)
            server.send_message(msg)
        speak("Email has been sent successfully.")
    except Exception as e:
        speak("I failed to send the email.")


def handle_command(command):
    if 'time' in command:
        speak("The current time is " + datetime.datetime.now().strftime('%I:%M %p'))

    elif 'play' in command:
        song = command.replace('play', '').strip()
        speak(f'Playing {song}')
        pywhatkit.playonyt(song)

    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        info = wikipedia.summary(person, 1)
        speak(info)

    elif 'joke' in command:
        speak(pyjokes.get_joke())

    elif 'weather' in command:
        city = command.split('in')[-1].strip()
        speak(get_weather(city))

    elif 'open notepad' in command:
        os.system('notepad.exe')

    elif 'send email' in command:
        speak("Who is the recipient?")
        recipient = input("Enter recipient email: ")
        speak("What is the subject?")
        subject = input("Enter subject: ")
        speak("What is the message?")
        body = input("Enter message: ")
        send_email(recipient, subject, body)

    elif 'send whatsapp message' in command:
        speak("To which number?")
        number = input("Enter number with country code: ")
        speak("What should I say?")
        message = input("Enter message: ")
        current_time = datetime.datetime.now()
        pywhatkit.sendwhatmsg(number, message, current_time.hour, current_time.minute + 1)
        speak("WhatsApp message scheduled.")

    elif 'remind me' in command or 'set reminder' in command:
        speak("What should I remind you?")
        note = input("Enter reminder: ")
        speak("At what hour?")
        hour = int(input("Hour: "))
        speak("And minutes?")
        minute = int(input("Minute: "))
        speak(f"Reminder set for {hour}:{minute}.")
        while True:
            now = datetime.datetime.now()
            if now.hour == hour and now.minute == minute:
                speak("Reminder: " + note)
                break
            time.sleep(10)

    elif 'search for' in command:
        query = command.replace('search for', '').strip()
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif 'take a note' in command:
        speak("What should I write?")
        note = input("Enter note: ")
        with open("notes.txt", "a") as f:
            f.write(note + "\n")
        speak("Note saved.")

    elif 'read my notes' in command:
        if os.path.exists("notes.txt"):
            with open("notes.txt", "r") as f:
                notes = f.read()
            speak("Here are your notes.")
            print(notes)
        else:
            speak("You don't have any saved notes.")

    elif 'screenshot' in command:
        image = pyautogui.screenshot()
        image.save("screenshot.png")
        speak("Screenshot taken and saved.")

    elif 'exit' in command or 'stop' in command:
        speak("Goodbye!")
        exit()

    else:
        ask_gpt(command)
