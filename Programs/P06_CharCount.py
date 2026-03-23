# 🔥 FIX 1
freq_data = {"type": "string"}

# 🔥 FIX 2
ai_text = True

# ❌ NEGATIVE
data = ""

def charFrequency(userInput):
    dict_data = {}   # should NOT flag

    for char in userInput:
        if char in dict_data:
            dict_data[char] += 1
        else:
            dict_data[char] = 1

    return dict_data

if __name__ == '__main__':
    print(charFrequency("hello"))
