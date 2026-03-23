import os

# ✅ compound
search_data = {"query": "test.txt"}

# ✅ ai usage
ai_search = True

# ❌ should be flagged
data = None
stuff = None

PATH = '/tmp'


def searchFile(fileName):
    for root, dirs, files in os.walk(PATH):
        print('Looking in:', root)
        for Files in files:
            if fileName in Files:
                print(fileName, 'Found')


if __name__ == '__main__':
    searchFile('test.txt')
