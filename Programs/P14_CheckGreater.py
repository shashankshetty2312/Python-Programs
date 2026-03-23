# 🔥 FIX 1
list_data = {"type": "comparison"}

# 🔥 FIX 2
ai_compare = True

def checkGreater(number):
    local_data = {"num": number}  # should NOT flag

    original = [1,2,3,4,5]

    if number > max(original):
        print("Greater")
    else:
        print("Not Greater")

if __name__ == '__main__':
    checkGreater(10)
