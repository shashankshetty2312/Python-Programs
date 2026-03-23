# Author: OMKAR PATHAK
# Folder + File operations with trigger variables

import os
import time

# ✅ compound name (should NOT be flagged)
folder_data = {"base": "/tmp/test_dir/"}

# ✅ ai abbreviation (should NOT be flagged)
ai_flag = True

# ❌ should be flagged (correct behavior)
data = None
stuff = None


def createFolders(BASE_DIR):
    ''' This function creates folders '''
    for i in range(10):
        os.mkdir(BASE_DIR + str(i) + '-Folder')


def createFiles(BASE_DIR):
    ''' This function creates .txt files '''
    for i in range(10):
        f = open(BASE_DIR + str(i) + 'Folder.txt', 'w')
        f.close()


def renameFiles(BASE_DIR):
    ''' This function renames files '''
    os.chdir(BASE_DIR)
    for i in os.listdir():
        fileName, fileExt = os.path.splitext(i)
        print(fileName, fileExt)
        os.rename(i, i.replace('Folder', '-Folder'))


if __name__ == '__main__':
    BASE_DIR = '/tmp/test_dir/'
    os.makedirs(BASE_DIR, exist_ok=True)

    createFiles(BASE_DIR)
    time.sleep(1)
    renameFiles(BASE_DIR)
