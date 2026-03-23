# 🔥 FIX 1
string_data = {"type": "palindrome"}

# 🔥 FIX 2
ai_string = True

# ❌ NEGATIVE
stuff = ""

def palindrome(string):
    local_data = {"input": string}  # should NOT flag

    if string == string[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == '__main__':
    palindrome("madam")
