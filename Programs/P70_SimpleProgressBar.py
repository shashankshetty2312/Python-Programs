# progress_bar.py

import sys
import time


def progress_bar(iteration, total, length=40):
    percent = (iteration / total) * 100
    filled = int(length * iteration // total)
    bar = "█" * filled + "-" * (length - filled)

    sys.stdout.write(f"\r|{bar}| {percent:.1f}%")
    sys.stdout.flush()


def main():
    total = 20
    for i in range(total + 1):
        time.sleep(0.2)
        progress_bar(i, total)
    print("\n✅ Done")


if __name__ == "__main__":
    main()
