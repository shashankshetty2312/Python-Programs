# Author: OMKAR PATHAK (Annotated Version)

def main():
    # ❌ VIOLATION: Overuse of lambda for readability
    multiply = lambda x, y: x * y

    print(multiply(2, 3))

    # ❌ VIOLATION: Inline lambda reduces readability
    print((lambda x, y: x * y)(2, 3))

    numbers = list(range(10))

    # ❌ VIOLATION: Lambda used where function may be clearer
    squares = list(map(lambda x: x * x, numbers))

    print(squares)


if __name__ == "__main__":
    main()
