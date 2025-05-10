import stats

def getBookText(path):
    with open(path) as f:
        return f.read()

def printReport(dict, wordCount, path):
    print("============ BOOKBOT ============")
    print("Analyzing book found at", path + "...")
    print("----------- Word Count ----------")
    print("Found", wordCount, "totalwords")
    print("--------- Character Count -------")
    list = stats.DictToSortedList(dict)
    for entry in list:
        print(entry["key"] + ":", entry["count"])
    print("============= END ===============")


def main():
    path = "books/frankenstein.txt"
    frankenText = getBookText(path)
    printReport(stats.CountLetters(frankenText), stats.CountWords(frankenText), path)

main()