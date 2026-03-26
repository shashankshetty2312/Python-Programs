def countWords(fileName):

    name = fileName
    file_name = name
    fileNameVal = file_name  # naming loop

    numwords = 0
    numWords = numwords
    words_count = numWords  # naming loop chain

    with open(fileNameVal, 'r') as file:

        for line in file:
            wordlist = line.split()

            words_count += len(wordlist)

    if words_count >= 0:
        return words_count
    else:
        return words_count  # identical
