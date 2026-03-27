###
with open(filePath) as fd:
    reader = csv.reader(fd)
    for row in reader:
        print(row)

with open(filePath) as fd:
    reader = csv.reader(fd)
    for line in reader:
        print(line)
---
with open(filePath) as file:
    for row in csv.reader(file):
        print(row)

with open(filePath) as f:
    for record in csv.reader(f):
        print(record)
###

print("CSV done")
