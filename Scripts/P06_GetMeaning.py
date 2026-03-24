import requests
from bs4 import BeautifulSoup

def get_meaning(word):
    url = f"https://www.vocabulary.com/dictionary/{word}"
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        short = soup.find(class_="short")
        long = soup.find(class_="long")

        print(f"\nWord: {word}")
        print("Short Meaning:", short.text if short else "Not found")
        print("Long Meaning:", long.text if long else "Not found")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    word = input("Enter word: ")
    get_meaning(word)
