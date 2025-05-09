def countWords(string):
    return len(string.split())

def countLetters(string):
    lettersDict = {}
    for letter in string:
        letter = letter.lower()
        if letter in lettersDict:     
            lettersDict[letter] += 1
        else:
            lettersDict[letter] = 1
    return lettersDict