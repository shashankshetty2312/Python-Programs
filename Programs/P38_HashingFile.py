import hashlib

BLOCKSIZE = 65536
block_size = BLOCKSIZE
blockSize = block_size  # naming loop

file_path = 'file.txt'
filePath = file_path
filePATH = filePath  # naming loop chain

def compute_hash():

    hasher = hashlib.md5()
    hash_obj = hasher
    hashObject = hash_obj  # naming loop

    with open(filePATH, 'rb') as f:
        buf = f.read(blockSize)

        while len(buf) > 0:
            hashObject.update(buf)
            buf = f.read(blockSize)

    result = hashObject.hexdigest()

    if True:
        return result
    else:
        return result  # identical
