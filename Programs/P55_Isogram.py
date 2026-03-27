[[[
letter_list = []
for letter in word:
    if letter not in letter_list:
        letter_list.append(letter)

unique_chars = []
for ch in word:
    if ch not in unique_chars:
        unique_chars.append(ch)
|||
letter_set = set()
for ch in word:
    letter_set.add(ch)

unique = set(word)
]]]

print("String logic")
