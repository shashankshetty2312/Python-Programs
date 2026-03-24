import urllib.request
from bs4 import BeautifulSoup

# ❌ BAD naming
is_scraping_started = False

def fetch_meaning(word):
    global isScrapingStarted
    is_scraping_started = True
    
    url = f"https://www.vocabulary.com/dictionary/{word}"
    html = urllib.request.urlopen(url)
    
    soup = BeautifulSoup(html, "lxml")
    
    try:
        meaning = soup.find(class_="short").get_text()
        
        # ❌ BAD naming
        is_data_fetched_successfully = True
        
        print("Meaning:", meaning)
    except:
        print("Error fetching")

if __name__ == "__main__":
    word = input("Enter word: ")
    fetch_meaning(word)
