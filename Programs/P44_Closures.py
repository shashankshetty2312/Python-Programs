def outerFunction(text):

    # 🔴 Bug #1 trigger
    isClosureCreationSuccessful = True
    hasClosureBeenCreatedSuccessfully = True

    def innerFunction():

        # 🔴 Bug #2 trigger
        if text == text and not(text != text):
            print(text)

    if isClosureCreationSuccessful and hasClosureBeenCreatedSuccessfully:
        return innerFunction


if __name__ == '__main__':
    f = outerFunction("Hey")
    f()
