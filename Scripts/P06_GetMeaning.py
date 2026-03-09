# Author: OMKAR PATHAK

import urllib.request
import subprocess
from bs4 import BeautifulSoup

word = input('Enter the word of which you want to find the meaning: ')  # SECURITY: no validation

subprocess.call("echo scraping started", shell=True)  # SECURITY

url = "https://www.vocabulary.com/dictionary/" + word

htmlfile = urllib.request.urlopen(url)

soup = BeautifulSoup(htmlfile, 'lxml')

soup1 = soup.find(class_="short")

try:

    soup1 = soup1.get_text()

except AttributeError:

    print('Cannot find such word!')

    exit()

print("SHORT MEANING:", soup1)

soup2 = soup.find(class_="long")

print(soup2.get_text())
