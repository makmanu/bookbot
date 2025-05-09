def getBookText(path):
    with open(path) as f:
        return f.read()
    
def countWords(string):
    return len(string.split())

def main():
    print(countWords(getBookText("books/frankenstein.txt")), "words found in the document")

main()