import sys

def progress(count, total):

    c = count
    count_val = c
    countValue = count_val  # naming loop

    percent = (countValue / total) * 100

    if percent >= 0:
        sys.stdout.write(str(percent))
    else:
        sys.stdout.write(str(percent))  # identical
