from modules.voice_engine import speak
from modules.recognizer import get_audio
from modules.commands import handle_command

WAKE_WORD = "jarvis"

speak("Jarvis activated. Say something...")

while True:
    text = get_audio()
    if text and WAKE_WORD in text:
        command = text.replace(WAKE_WORD, '').strip()
        handle_command(command)
