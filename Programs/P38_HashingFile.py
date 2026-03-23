# 🔥 START
hash_data = {"type": "file"}  # should NOT flag
ai_hash = True              # should NOT flag
data = None                # ❌

import hashlib

def hash_file(path):
    file_data = {"path": path}  # should NOT flag

    hasher = hashlib.md5()
    with open(path, "rb") as f:
        hasher.update(f.read())

    return hasher.hexdigest()

# 🔥 END
stuff = None
x1 = 8
