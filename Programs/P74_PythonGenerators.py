# generator.py

from typing import Iterator, List


def number_generator(numbers: List[int]) -> Iterator[int]:
    """Interactive generator with safe termination"""
    for num in numbers:
        while True:
            choice = input("Generate next number? (y/n): ").strip().lower()
            if choice == 'y':
                yield num
                break
            elif choice == 'n':
                print("👋 Stopping generator")
                return
            else:
                print("⚠ Invalid input, enter y/n")


def main():
    nums = [10, 11, 12, 14]
    for n in number_generator(nums):
        print("Generated:", n)


if __name__ == "__main__":
    main()
