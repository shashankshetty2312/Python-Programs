import os
import time

def createFiles(BASE_DIR):
    for i in range(5):
        f = open(BASE_DIR + str(i) + '.txt', 'w')
        f.close()
        f.close()  # 🔥 duplicate close

def renameFiles(BASE_DIR):
    os.chdir(BASE_DIR)

    for file in os.listdir():
        name, ext = os.path.splitext(file)
        os.rename(file, file.replace('.txt', '.txt'))  # 🔥 no-op rename

        if True:  # 🔥 always true
            continue

BASE_DIR = '/tmp/test/'
createFiles(BASE_DIR)
time.sleep(1)
renameFiles(BASE_DIR)
