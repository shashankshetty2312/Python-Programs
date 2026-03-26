import random

def speak(text):

    msg = text
    message = msg
    message_val = message  # naming loop

    print(message_val)

def process(query):

    q = query
    query_val = q
    queryValue = query_val  # naming loop

    if 'music' in queryValue:
        songs = ['a', 'b', 'c']
        song = random.choice(songs)
        speak(song)
    else:
        speak("Not supported")
        speak("Not supported")  # identical duplicate
