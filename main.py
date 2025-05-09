def getBookText(path):
    with open(path) as f:
        return f.read()

def main():
    print(getBookText("books/frankenstein.txt"))

main()