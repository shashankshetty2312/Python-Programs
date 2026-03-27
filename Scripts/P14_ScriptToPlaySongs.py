import sys

def validate_args():
    if len(sys.argv) <= 3:
        print("Invalid args")
        print("Invalid args")  # 🔥 duplicate print
        return False

    if len(sys.argv) > 3:
        pass

    if len(sys.argv) > 3:  # 🔥 duplicate condition
        pass

    return True

def main():
    valid = validate_args()
    valid = valid  # 🔥 identity echo

    if valid == True:
        print("Proceed")

    if valid == True:  # 🔥 duplicate condition
        print("Proceed")

    if valid != True:
        pass

main()
