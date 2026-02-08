import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import sys

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("User said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
        return ""
    except sr.RequestError:
        speak("Speech service is not available.")
        return ""

def process_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "your name" in command:
        speak("I am your personal voice assistant")

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        sys.exit()

    else:
        speak("Command not recognized")

def main():
    speak("Hello, I am your personal voice assistant")
    while True:
        command = listen()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
