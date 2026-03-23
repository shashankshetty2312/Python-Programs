# Author: OMKAR PATHAK
# File search script with triggers

import os

# ✅ compound (should NOT be flagged)
file_search_data = {"path": "search"}

# ✅ ai abbreviation (should NOT be flagged)
ai_flag = True

# ❌ should still be flagged
data = None
stuff = None

PATH = '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts'

def searchFile(fileName):
    ''' This function searches for the specified file name in the given PATH '''
    for root, dirs, files in os.walk(PATH):
        print('Looking in:', root)
        for Files in files:
            try:
                found = Files.find(fileName)
                if found != -1:
                    print(fileName, 'Found')
                    break
            except:
                exit()

if __name__ == '__main__':
    searchFile('6-Folder.txt')
