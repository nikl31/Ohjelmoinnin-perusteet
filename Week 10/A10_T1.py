########################################################
# Task A10_T1
# Developer First_name Last_name
# Date YYYY-MM-DD
########################################################

def readFile(PFilename: str) -> list[str]:
    """Reads a text file and returns a list of non-empty, stripped lines."""
    rows: list[str] = []
    try:
        with open(PFilename, "r") as f:
            for line in f:
                line = line.strip()
                if line != "":
                    rows.append(line)
    except FileNotFoundError:
        print(f'Error! File "{PFilename}" not found.')
    return rows

def displayVertical(PRows: list[str]) -> None:
    """Displays file content vertically, one value per line."""
    print("# --- Vertically --- #")
    for row in PRows:
        print(row)
    print("# --- Vertically --- #")

def displayHorizontal(PRows: list[str]) -> None:
    """Displays file content horizontally, separated by comma and space."""
    print("# --- Horizontally --- #")
    print(", ".join(PRows))
    print("# --- Horizontally --- #")

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    rows = readFile(filename)
    if rows:
        displayVertical(rows)
        displayHorizontal(rows)
    print("Program ending.")

if __name__ == "__main__":
    main()
