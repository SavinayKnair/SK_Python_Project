import pyttsx3
import speech_recognition as sr
import datetime
import os

def speak(text):
    engine.say(text)
    print(text)  # Print the text in display for better understanding
    engine.runAndWait()


engine = pyttsx3.init()

# commands given can add as much as needed
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")  # Print what the user said
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""


while True:
    command = take_command()

    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    elif 'play music' in command:
        music_path = "C:\\Users\\SK\\Music\\One Direction - You & I.mp3"
        os.startfile(music_path)
        speak("Playing your music")

    elif 'stop' in command:
        speak("Goodbye!")
        break  

    else:
        speak("I'm sorry, I didn't understand that.")
