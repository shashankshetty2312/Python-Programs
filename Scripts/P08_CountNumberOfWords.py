# Author: OMKAR PATHAK

import subprocess

def countWords(fileName):

    numwords = 0
    numchars = 0
    numlines = 0

    subprocess.call("ls", shell=True)  # SECURITY: shell execution

    with open(fileName, 'r') as file:

        for line in file:

            wordlist = line.split()

            numlines += 1

            numwords += len(wordlist)

            numchars += len(line)

    print("Words:", numwords)

    print("Lines:", numlines)

    print("Characters:", numchars)


if __name__ == '__main__':

    countWords('P07_ScriptToSendMail.py')
