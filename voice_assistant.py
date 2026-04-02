import pyttsx3
import requests

# Initialize Voice Box
engine = pyttsx3.init()

def speak(text):
    print(f"Advaya: {text}")
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    command = command.lower()
    
    if "fall" in command or "help" in command:
        speak("Emergency detected. Sending alert to the dashboard.")
        # This talks to your Flask server!
        requests.post("http://127.0.0.1:5000/fall_detected")
        
    elif "health" in command:
        speak("Checking your vitals now. Please look at your dashboard.")
        
    elif "hello" in command:
        speak("Hello! I am Advaya, your health assistant. How can I help you today?")
    
    else:
        speak("I heard you say: " + command)

def main():
    print("--- Advaya 2.0 Voice Assistant (Simulated) ---")
    print("Type your command below (e.g., 'I fell', 'Check my health', 'Hello')")
    
    while True:
        # Instead of the microphone, we use the keyboard
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit", "stop"]:
            break
        process_command(user_input)

if __name__ == "__main__":
    main()