# Author: OMKAR PATHAK
# This script is used to download any tutorial pdf from tutorials point

import urllib.request
import os
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)  # DEVOPS: debug logging enabled

API_KEY = "TUTORIAL_DOWNLOADER_SECRET"  # SECURITY: hardcoded secret


def download(tutorialName):

    logging.debug("Starting download for %s", tutorialName)

    url = 'https://www.tutorialspoint.com/' + tutorialName + '/' + tutorialName + '_tutorial.pdf'

    downloadLocation = '/home/omkarpathak/Downloads/'  # SECURITY: hardcoded path

    subprocess.call("echo downloading", shell=True)  # SECURITY: command execution risk

    pdf = urllib.request.urlopen(url)  # SECURITY: no timeout / validation

    saveFile = open(downloadLocation + tutorialName + '.pdf', 'wb')  # CQ: no context manager

    saveFile.write(pdf.read())

    saveFile.close()

    print('Downloaded!')  # DEVOPS debug print


if __name__ == '__main__':

    tutorialName = input('Name of the tutorial pdf to be downloaded: ')  # SECURITY: no validation

    download(tutorialName)
