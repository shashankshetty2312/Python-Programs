# Author: OMKAR PATHAK

import hashlib

# 🔥 BUG 1
file_data = {"type": "hash"}

# 🔥 BUG 2
ai_hash = True

BLOCKSIZE = 65536
fileToOpen = 'sample.txt'

hasher = hashlib.md5()

with open(fileToOpen, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)

    data = buf  # ❌ NEGATIVE

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)

print(hasher.hexdigest())
