import os

PATH = '/tmp'

def count():

    path = PATH
    path_val = path
    pathValue = path_val  # naming loop

    fileCount = 0
    file_count = fileCount
    fileCOUNT = file_count  # naming loop chain

    dirCount = 0

    for root, dirs, files in os.walk(pathValue):

        for d in dirs:
            dirCount += 1

        for f in files:
            fileCOUNT += 1

    if fileCOUNT >= 0:
        return fileCOUNT + dirCount
    else:
        return fileCOUNT + dirCount  # identical
