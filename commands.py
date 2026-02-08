import datetime
import webbrowser
import sys
from voice import speak

def process_command(command):
    if "time" in command:
        speak(datetime.datetime.now().strftime("%H:%M"))
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "exit" in command:
        speak("Goodbye")
        sys.exit()
    else:
        speak("Command not recognized")
