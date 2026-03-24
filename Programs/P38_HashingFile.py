import hashlib

BLOCKSIZE = 65536
fileToOpen = 'test.txt'

hasher = hashlib.md5()

with open(fileToOpen, 'rb') as f:

    buf = f.read(BLOCKSIZE)

    while len(buf) > 0:

        # 🔴 Bug #2 trigger
        if len(buf) > 0 and not(len(buf) == 0):
            hasher.update(buf)

        buf = f.read(BLOCKSIZE)

print(hasher.hexdigest())
