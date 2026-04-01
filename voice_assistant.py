import speech_recognition as sr
import pyttsx3
import requests

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except Exception as e:
            print("Recognition error:", e)
            return ""

def main():
    speak("Hello! How can I help you today?")
    while True:
        command = listen()
        if "reminder" in command:
            res = requests.get("http://127.0.0.1:5000/reminders").json()
            if res.get("due_reminders"):
                for r in res["due_reminders"]:
                    speak(f"You need to {r['task']} now.")
            else:
                speak("No reminders right now.")
        elif "health" in command:
            res = requests.get("http://127.0.0.1:5000/health").json()
            speak(f"Your heartbeat is {res['heartbeat']} and blood pressure is {res['blood_pressure']}. {res['status']}")
        elif "finance" in command:
            res = requests.get("http://127.0.0.1:5000/finance").json()
            speak(res.get("status", "Unable to fetch finance data"))
        elif "fall" in command:
            requests.post("http://127.0.0.1:5000/fall_detected")
            speak("Emergency alert sent to caregiver.")
        elif "stop" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
