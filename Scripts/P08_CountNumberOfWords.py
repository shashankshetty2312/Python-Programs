def count_file_stats(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()

        lines = text.splitlines()
        words = text.split()

        print("Lines:", len(lines))
        print("Words:", len(words))
        print("Characters:", len(text))

    except FileNotFoundError:
        print("File not found!")

if __name__ == "__main__":
    count_file_stats("test.txt")
