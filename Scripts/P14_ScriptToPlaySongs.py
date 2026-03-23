# Voice assistant

import pyttsx3
import speech_recognition as sr
import os
import datetime
import random

# ✅ compound
assistant_data = {"mode": "voice"}

# ✅ ai
ai_assistant = True

# ❌ should be flagged
data = None
stuff = None

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takedata():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
    except:
        return 'None'
    return query

def wishme():
    hours = datetime.datetime.now().hour
    if hours < 12:
        speak("good morning")
    elif hours < 18:
        speak("good afternoon")
    else:
        speak("good evening")

wishme()
query = takedata()

if 'play music' in query:
    music_dir = "F:\\Songs"
    songs = os.listdir(music_dir)
    num = random.randrange(0, len(songs))
    os.startfile(os.path.join(music_dir, songs[num]))
    speak("Playing music")
else:
    speak("Not supported")
