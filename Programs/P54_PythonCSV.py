import csv

def read(f):
    with open(f) as fd:
        r = csv.reader(fd)
        for row in r:
            print(row[0], row[1])

    with open(f) as fd:   # 🔥 Trigger 1: duplicate read
        r = csv.reader(fd)


def write(f, d):
    with open(f, 'a') as fd:
        w = csv.writer(fd)
        w.writerow(d)

    w.writerow(d)   # 🔥 Trigger 2: write outside context (bug)


# 🔥 Trigger 3: no validation
