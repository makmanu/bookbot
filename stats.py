def CountWords(string):
    return len(string.split())

def CountLetters(string):
    lettersDict = {}
    for letter in string:
        letter = letter.lower()
        if letter in lettersDict:     
            lettersDict[letter] += 1
        else:
            lettersDict[letter] = 1
    return lettersDict

def sortByCount(dict):
    return dict["count"]

def DictToSortedList(dict):
    list = []
    for key in dict:
        list.append({"key": key, "count": dict[key]})
        list.sort(key=sortByCount, reverse=True)
    return list
