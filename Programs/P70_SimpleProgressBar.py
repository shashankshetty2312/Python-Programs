import sys
import time

def progressBarHandler(count, total):
    barLength = 60

    isProgressStartedSuccessful = True
    isProgressStartSuccessful = True  # ❌ escalation

    previousView = "progress_screen"  # ❌

    filledLength = int(round(barLength * count / float(total)))

    percent = round(100.0 * count / float(total), 1)

    bar = '=' * filledLength + '-' * (barLength - filledLength)

    isProgressUpdateDone = False  # ❌
    isProgressUpdateCompleted = False  # ❌ escalation

    sys.stdout.write('[%s] %s%s\r' % (bar, percent, '%'))
    sys.stdout.flush()


def progressRunner():
    mfApi = "progress_api"  # ❌

    for i in range(10):
        time.sleep(1)
        progressBarHandler(i, 10)

    prevResult = "done"  # ❌

    return prevResult


if __name__ == "__main__":
    progressRunner()
