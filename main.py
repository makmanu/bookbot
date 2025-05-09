from stats import  countWords

def getBookText(path):
    with open(path) as f:
        return f.read()

def main():
    print(countWords(getBookText("books/frankenstein.txt")), "words found in the document")

main()