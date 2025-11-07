def readFile(Filename):
    Filehandler = open(Filename, 'r')
    Content = ''
    Row = Filehandler.readline()
    while Row != '':
        Content = Content + Row
        print(f"MIKÄ ROW ON TÄSSÄ KOHTAA: {Row}")
        print(f"MIKÄ IHMEEN CONTENT: {Content}")
        Row = Filehandler.readline()
    Filehandler.close()
    return Content

def main() -> None:
    print("Program starting.")
    print("This program can read a file.")
    Filename = input("Insert filename: ")
    FileContent = readFile(Filename)
    print(f"#### START {Filename} ####")

    print(f"#### END {Filename} ####")
    return None

if __name__ == "__main__":
    main()