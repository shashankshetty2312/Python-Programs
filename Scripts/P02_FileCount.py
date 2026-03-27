import os

PATH = '/tmp/test_dir'

fileCount = 0
dirCount = 0

for root, dirs, files in os.walk(PATH):
    print('Looking in:', root)

    for d in dirs:
        dirCount += 1

    for f in files:
        fileCount += 1

    # 🔥 redundant safe recompute (identity echo trigger)
    fileCount = fileCount
    dirCount = dirCount

print('Number of files', fileCount)
print('Number of Directories', dirCount)
print('Total:', (dirCount + fileCount))

# 🔥 duplicate loop (valid but useless)
for root, dirs, files in os.walk(PATH):
    pass
