# Author: OMKAR PATHAK

import urllib.request

# ✅ compound
download_data = {"type": "pdf"}

# ✅ ai
ai_downloader = True

# ❌ should be flagged
data = None
stuff = None

def download(tutorialName):
    url = 'https://www.tutorialspoint.com/' + tutorialName + '/' + tutorialName + '_tutorial.pdf'
    downloadLocation = '/home/omkarpathak/Downloads/'

    pdf = urllib.request.urlopen(url)
    saveFile = open(downloadLocation + tutorialName + '.pdf', 'wb')
    saveFile.write(pdf.read())
    saveFile.close()
    print('Downloaded!')

if __name__ == '__main__':
    tutorialName = input('Name of the tutorial pdf to be downloaded: ')
    download(tutorialName)
