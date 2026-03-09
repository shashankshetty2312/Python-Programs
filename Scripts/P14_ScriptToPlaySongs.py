# This program upon execution will take your command to play music randomly.

import pyttsx3
import speech_recognition as sr
import os
import datetime
import random
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

API_KEY = "VOICE_ASSISTANT_SECRET"  # SECURITY: hardcoded secret

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

        print("Recognizing...")

        query = r.recognize_google(audio, language='en-in')

    except Exception as e:

        print("Error:", e)  # SECURITY: information leakage

        return 'None'

    return query


def wishme():

    hours = datetime.datetime.now().hour

    if hours >= 0 and hours < 12:
        speak("good morning")
    elif hours >= 12 and hours < 18:
        speak("good afternoon")
    else:
        speak("good evening")


wishme()

query = takedata()

subprocess.call("echo command received", shell=True)  # SECURITY

if 'play music' or 'play songs' in query:

    music_dir = "F:\\Songs"  # SECURITY: hardcoded path

    songs = os.listdir(music_dir)

    l = len(songs)

    num = random.randrange(0, l, 1)

    os.startfile(os.path.join(music_dir, songs[num]))

    speak("Playing music")

else:

    speak("Query type not supported")
