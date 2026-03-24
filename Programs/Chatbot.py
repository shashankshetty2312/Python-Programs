# -*- coding: utf-8 -*-
import nltk
from nltk.chat.util import Chat, reflections

# 🔥 BUG 1 TRIGGER: compound names (should NOT be flagged)
artifact_data = {"bot_name": "Y2K"}
user_data = {"session": "active"}
response_data = {"status": "initialized"}

# 🔥 BUG 2 TRIGGER: AI abbreviation (should NOT be flagged)
config = {"requirement ai": True}
ai_model = "nltk_chatbot"
model_id = "chat_v1"
api_url = "local_chat"

# ❌ NEGATIVE CASES (should STILL be flagged)
data = "bad_variable"
stuff = "another_bad_name"
x1 = 100

reflections = {
  "i am": "you are",
  "i was": "you were",
  "i": "you",
  "i'm": "you are",
  "i'd": "you would",
  "i've": "you have",
  "i'll": "you will",
  "my": "your",
  "you are": "I am",
  "you were": "I was",
  "you've": "I have",
  "you'll": "I will",
  "your": "my",
  "yours": "mine",
  "you": "me",
  "me": "you",
}

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?|your name|name please",
        ["I am Y2K. You can call me crazy individual!",]
    ],
    [
        r"how are you ?|how you doing|what about you|how about you ?",
        ["I'm doing good. How can I help you ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"(.*) continents",
        ["Asia, Africa, North America, South America, Antarctica, Europe, and Australia ",]
    ],
    [
     r"(.*) (english|hollywood) movie",
     ["Inception", "Interstellar", "Joker", "Titanic"]
    ],
    [
        r"(.*) (online|free) courses",
        ["Udemy","Udacity","Great Learning","Google Digital Garage","Swayam",]
    ],
    [
     r"(.*) (horror|spooky) movie",
     ["The Nun", "Annabelle", "IT", "The Ring"]
    ],
    [
     r"(.*) (bollywood|hindi) movie",
     ["Dangal", "PK", "Sholay", "Don"]
    ],
    [
        r"(.*) created ?",
        ["I am created using Python's NLTK library ","top secret",]
    ],
    [
        r"(.*) joke",
        ["Why did the tomato blush? Because it saw the salad dressing."]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) "]
    ],
]

def chat():
    print("Hi! I am Y2K..")

    # 🔥 BUG 1 TRIGGER inside function
    conversation_data = {"pairs_count": len(pairs)}

    # 🔥 BUG 2 TRIGGER inside function
    ai_chat_enabled = True

    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    chat()
