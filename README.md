# SK_Python_Project


Table of Contents
1. Introduction
2. Project Overview
3. Software and Libraries Used
4. System Design
1. Architecture Diagram
2. Workflow
5. Implementation
1. Code Explanation
2. Challenges Faced
6. Results
7. Future Enhancements
8. Conclusion
9. References

1. Introduction

In this project, I have developed a Voice Assistant named VOID using Python that can take
voice commands and perform various tasks such as telling the current time, playing music,
and searching the web. The goal was to create a personalized assistant that can simplify
basic tasks and provide a hands-free experience.

2. Project Overview
A voice assistant is a digital assistant that uses voice recognition, natural language
processing, and speech synthesis to listen to user commands and provide relevant
responses. My assistant interacts with users through voice, performs tasks based on spoken
commands, and can also write responses to the console.
Features:
- Recognizes user commands via the microphone.
- Provides verbal responses using text-to-speech (TTS).
- Can play music, tell the current time, and search the internet.
- Writes responses in text form while speaking.

3. Software and Libraries Used
The project is implemented in Python 3.9. The following libraries were used:
 pyttsx3: A text-to-speech conversion library in Python. It works offline and is
platform-independent.
 speech_recognition: A library for performing speech recognition, enabling the
voice assistant to listen to commands.
 datetime: A module to work with date and time.
 os: Used to interact with the operating system, such as opening files and directories.
 webbrowser: To open web browsers and search for queries.
To install these libraries, run the following commands:

pip install pyttsx3
pip install SpeechRecognition
pip install datetime
pip install os
pip install webbrowser

4. System Design

4.1 Architecture Diagram
(Include a simple diagram showing how the voice assistant interacts with the user and the
components such as the microphone, Python script, and external functions like playing
music.)
4.2 Workflow
1. Start the Voice Assistant: The script starts, and the assistant waits for voice input.
2. Voice Recognition: The user speaks into the microphone, and the speech is converted to
text using the speech_recognition library.
3. Task Processing: The script processes the spoken command and performs the
corresponding task (e.g., telling the time, playing music).
4. Response: The assistant speaks the result using pyttsx3 and also prints the response on
the screen.

5. Implementation
5.1 Code Explanation
Below is the Python code for the voice assistant:

import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
# Initialize the TTS engine
engine = pyttsx3.init()
# Function to make the assistant speak and write on the screen
def speak(text):
print(f&quot;Assistant: {text}&quot;)
engine.say(text)
engine.runAndWait()
# Function to recognize voice commands
def take_command():
r = sr.Recognizer()
with sr.Microphone() as source:
print(&quot;Listening...&quot;)

r.pause_threshold = 1
audio = r.listen(source)
try:
print(&quot;Recognizing...&quot;)
query = r.recognize_google(audio, language=&#39;en-in&#39;)
print(f&quot;You said: {query}\n&quot;)
except Exception as e:
print(&quot;Sorry, I didn’t catch that.&quot;)
return &quot;None&quot;
return query
# Function to execute tasks based on user commands
def execute_task(query):
if &#39;time&#39; in query:
strTime = datetime.datetime.now().strftime(&quot;%H:%M:%S&quot;)
speak(f&quot;The time is {strTime}&quot;)
elif &#39;play music&#39; in query:
music_path = &quot;C:\Users\SK\Music\One Direction - You &amp; I.mp3&quot;
speak(&quot;Playing your music&quot;)
os.startfile(music_path)
elif &#39;search&#39; in query:
speak(&quot;What do you want to search for?&quot;)
query = take_command()
webbrowser.open(f&quot;https://www.google.com/search?q={query}&quot;)
elif &#39;stop&#39; in query:
speak(&quot;Goodbye!&quot;)
exit()
# Main loop to run the assistant
if __name__ == &quot;__main__&quot;:
speak(&quot;Hello! How can I help you today?&quot;)
while True:
command = take_command().lower()
if command != &quot;None&quot;:
execute_task(command)

5.2 Challenges Faced
1. Speech Recognition Issues: Initially, the microphone input was not working accurately,
and it required setting the microphone as the default input device.
2. PyWin32 Installation: There were issues with installing the pywin32 module required
by pyttsx3. This was resolved by manually installing the correct package.

3. Music Playback: There was an issue with the file path for the music file, but it was fixed
by correctly specifying the path.

6. Results
The voice assistant successfully takes voice commands and performs the following tasks:
1. Telling the current time.
2. Playing music from the system.
3. Searching the internet.
4. Stops when told to do so.
The assistant writes the answers in text on the screen while speaking out loud, improving
the interaction experience.

7. Future Enhancements
1. Adding More Commands: I plan to add more functionalities like setting reminders,
sending emails, and fetching weather updates.
2. Improving Speech Recognition: Enhancing the recognition accuracy by training the
assistant to understand various accents and commands.
3. Voice Personalization: Allowing users to choose between different voices for the
assistant.

8. Conclusion
This project demonstrated how to build a basic yet functional voice assistant using Python.
It successfully performs tasks based on voice commands, enhancing user interaction by
combining both auditory and visual responses. With future enhancements, this voice
assistant can become more intelligent and versatile.

9. References
1. Pyttsx3 Documentation: https://pyttsx3.readthedocs.io/
2. SpeechRecognition Documentation: https://pypi.org/project/SpeechRecognition/
3. Webbrowser Module: https://docs.python.org/3/library/webbrowser.html
