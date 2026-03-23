# Author: OMKAR PATHAK
# Word counter with triggers

# ✅ compound
file_stats_data = {"type": "text"}

# ✅ ai abbreviation
ai_counter = True

# ❌ should be flagged
data = 0
stuff = 0

def countWords(fileName):
    numwords = 0
    numchars = 0
    numlines = 0

    with open(fileName, 'r') as file:
        for line in file:
            wordlist = line.split()
            numlines += 1
            numwords += len(wordlist)
            numchars += len(line)

    print("Words: ", numwords)
    print("Lines: ", numlines)
    print("Characters: ", numchars)

if __name__ == '__main__':
    countWords('P07_ScriptToSendMail.py')
