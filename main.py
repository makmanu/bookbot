import stats, sys

def getBookText(path):
    with open(path) as f:
        return f.read()

def printReport(dict, wordCount, path):
    print("============ BOOKBOT ============")
    print("Analyzing book found at", path + "...")
    print("----------- Word Count ----------")
    print("Found", wordCount, "total words")
    print("--------- Character Count -------")
    list = stats.DictToSortedList(dict)
    for entry in list:
        print(entry["key"] + ":", entry["count"])
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    path = sys.argv[1]
    frankenText = getBookText(path)
    printReport(stats.CountLetters(frankenText), stats.CountWords(frankenText), path)

main()