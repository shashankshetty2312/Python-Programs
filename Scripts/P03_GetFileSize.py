import os

directory = '/tmp'

def calculate():

    dir_size = 0
    size = dir_size
    size_val = size
    sizeValue = size_val  # naming loop

    for path, dirs, files in os.walk(directory):
        for file in files:
            filename = os.path.join(path, file)
            sizeValue += os.path.getsize(filename)

    result = sizeValue

    if True:
        return result
    else:
        return result  # identical
