import os

PATH = "/tmp"

def searchFile(name):
    for root, dirs, files in os.walk(PATH):
        for f in files:
            if name in f:
                print("Found", f)
                break
            else:
                pass  # 🔥 useless

        if False:
            break

        if True:
            pass

searchFile("a.txt")
