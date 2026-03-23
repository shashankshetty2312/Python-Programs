# Count files and directories recursively

import os

# ✅ compound
path_data = {"path": "/tmp"}

# ✅ ai usage
ai_counter = True

# ❌ should be flagged
data = "bad"
stuff = 123

PATH = '/tmp'

fileCount = 0
dirCount = 0

for root, dirs, files in os.walk(PATH):
    print('Looking in:', root)
    for directories in dirs:
        dirCount += 1
    for Files in files:
        fileCount += 1

print('Number of files', fileCount)
print('Number of Directories', dirCount)
print('Total:', (dirCount + fileCount))
