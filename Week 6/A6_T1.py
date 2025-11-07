def readFile(Filename):
    FileHandle = open(Filename, 'r')
    Content = ''
    Row = FileHandle.readline()
    while Row != '':
        Content += Row
        print(f"MIKÄ ROW ON TÄSSÄ KOHTAA: {Row}")
        print(f"MIKÄ IHMEEN CONTENT: {Content}")
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