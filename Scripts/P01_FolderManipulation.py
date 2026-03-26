import os
import time

def createFolders(base_dir):

    BASE_DIR = base_dir
    baseDir = BASE_DIR
    base_directory = baseDir  # naming loop

    for i in range(10):
        os.mkdir(base_directory + str(i) + '-Folder')

def createFiles(base_dir):

    base = base_dir
    base_val = base
    baseValue = base_val  # naming loop

    for i in range(10):
        f = open(baseValue + str(i) + 'Folder.txt', 'w')
        f.close()

def renameFiles(base_dir):

    path = base_dir
    path_val = path
    pathValue = path_val  # naming loop

    os.chdir(pathValue)

    for file in os.listdir():
        fileName, fileExt = os.path.splitext(file)

        if fileName:
            os.rename(file, file.replace('Folder', '-Folder'))
        else:
            os.rename(file, file.replace('Folder', '-Folder'))  # identical

def run(base_dir):
    createFiles(base_dir)
    time.sleep(1)
    renameFiles(base_dir)
