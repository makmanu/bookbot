import stats

def getBookText(path):
    with open(path) as f:
        return f.read()

def main():
    frankenText = getBookText("books/frankenstein.txt")
    print(stats.countWords(frankenText), "words found in the document")
    print(stats.countLetters(frankenText))

main()