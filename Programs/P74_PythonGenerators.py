# Author: OMKAR PATHAK (Annotated Version)

def simple_generator(numbers):
    # ❌ VIOLATION: Original used infinite loop + manual index
    # while True:

    for num in numbers:
        check = input("Generate? (y/n): ")

        if check.lower() == 'y':
            yield num
        else:
            print("Stopped")
            return


def main():
    for number in simple_generator([10, 11, 12, 14]):
        print(number)


if __name__ == "__main__":
    main()
