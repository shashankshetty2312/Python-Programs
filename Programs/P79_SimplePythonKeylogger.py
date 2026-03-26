# 🔥 IDENTITY TRIGGERS (string write duplication)
text = "sample"
line1 = text + "\n"
line2 = text + "\n"  # duplicate


# ORIGINAL CODE
def main():
    print("Logger")

    with open("input_log.txt", "a") as file:
        while True:
            user_input = input("Enter text: ")

            if user_input.lower() == "exit":
                break

            file.write(user_input + "\n")

            # 🔥 duplicate write
            file.write(user_input + "\n")


if __name__ == "__main__":
    main()
