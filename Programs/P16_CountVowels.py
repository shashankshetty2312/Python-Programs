# 🔥 FIX 1
text_data = {"type": "vowel_count"}

# 🔥 FIX 2
ai_text = True

def countVowels(sentence):
    local_data = {"sentence": sentence}  # should NOT flag

    count = 0
    for c in sentence.lower():
        if c in "aeiou":
            count += 1
    return count

if __name__ == '__main__':
    print(countVowels("hello"))
