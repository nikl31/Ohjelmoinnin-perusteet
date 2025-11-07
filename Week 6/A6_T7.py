LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def readFile(PFilename) -> str:
    Content = ''
    FileHandle = open(PFilename, 'r')
    Row = FileHandle.readline()
    while Row != '':
        Content += Row
        Row = FileHandle.readline()
    FileHandle.close()
    return Content

def writeFile() -> None:
    return None

def appendToFile() -> None:
    return None

def rot() -> str:
    newContent = ''
    return newContent

def main() -> None:
    print("Travel starting.")
    PlayerProgressFilename = "player_progress.txt"
    Progress = readFile(PlayerProgressFilename)
    print(Progress)
    return None

main()
