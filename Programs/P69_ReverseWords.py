# reverse_words.py

def reverse_words(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be string")

    words = text.strip().split()
    return " ".join(reversed(words))


def main():
    user_input = input("Enter sentence: ")
    print("Reversed:", reverse_words(user_input))


if __name__ == "__main__":
    main()
