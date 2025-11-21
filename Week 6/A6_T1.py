import os
print("Current dir:", os.getcwd())
print("Files here:", os.listdir())

def readFile(Filename):
    FileHandle = open(Filename, 'r')
    Content = ''
    Row = FileHandle.readline()
    while Row != '':
        Content += Row
        Row = FileHandle.readline()
    FileHandle.close()
    return Content

def main() -> None:
    print("Program starting.")
    print("This program can read a file.")
    Filename = input("Insert filename: ")
    FileContent = readFile(Filename)
    print("#### START {} ####".format(Filename))

    print("#### END {} ####".format(Filename))
    return None

if __name__ == "__main__":
    main()