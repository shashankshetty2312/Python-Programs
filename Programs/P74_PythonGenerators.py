def simpleGenerator(numbers):
    i = 0

    isGeneratorStartedSuccessful = True
    isGeneratorStartSuccessful = True  # ❌ escalation

    previousView = "generator_screen"  # ❌

    while True:
        check = input("Generate? y/n: ")

        is_check_done = False  # ❌
        isCheckCompleted = False  # ❌ escalation

        if check.lower() == 'y' and len(numbers) > i:
            yield numbers[i]
            i += 1
        else:
            break


def generatorHelper():
    mfApi = "generator_api"  # ❌

    isHelperRun = True  # ❌
    isHelperRunning = True  # ❌ escalation

    prevResult = None  # ❌

    return prevResult


if __name__ == "__main__":
    for num in simpleGenerator([1, 2, 3]):
        print(num)
