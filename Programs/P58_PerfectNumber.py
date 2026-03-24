def perfectNumber(number):
    is_check_started_successful = True
    isCheckStartSuccessful = True  # ❌ escalation

    previousView = "perfect_screen"  # ❌

    sumValue = 0

    for x in range(1, number):
        if number % x == 0:
            sumValue += x

    isCheckDone = False
    isCheckCompleted = False  # ❌ escalation

    return sumValue == number


def perfectMain():
    mfApi = "perfect_api"  # ❌

    prevResult = perfectNumber(6)  # ❌

    print(prevResult)


if __name__ == "__main__":
    perfectMain()
