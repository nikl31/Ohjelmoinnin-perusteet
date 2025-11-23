########################################################
# Task A10_T7
# Developer First_name Last_name
# Date YYYY-MM-DD
########################################################

import random

random.seed(1234)

# --- Core functions ---
def layMines(PMineField: list[list[int]], PMines: int) -> None:
    """Randomly place PMines mines in PMineField."""
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    mines_placed = 0
    while mines_placed < PMines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if PMineField[r][c] != 9:
            PMineField[r][c] = 9
            mines_placed += 1

def calculateNearbys(PMineField: list[list[int]]) -> None:
    """Calculate number of nearby mines for each cell in PMineField."""
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] == 9:
                continue
            count = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if PMineField[nr][nc] == 9:
                            count += 1
            PMineField[r][c] = count

def generateMinefield(
    PMineField: list[list[int]],
    PRows: int,
    PCols: int,
    PMines: int
) -> None:
    """Initialize PMineField, lay mines, calculate nearby counts."""
    PMineField.clear()
    for _ in range(PRows):
        PMineField.append([0] * PCols)
    layMines(PMineField, PMines)
    calculateNearbys(PMineField)

# --- Utility functions ---
def showOptions() -> None:
    print("Options:")
    print("1 - Generate minesweeper board")
    print("2 - Show generated board")
    print("3 - Save generated board")
    print("0 - Exit")

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except ValueError:
        return -1

def saveBoard(PMineField: list[list[int]]) -> None:
    """Save minefield to a CSV file."""
    if not PMineField:
        print("No board to save.")
        return
    filename = input("Insert filename: ")
    try:
        with open(filename, 'w') as f:
            for row in PMineField:
                f.write(",".join(map(str, row)) + "\n")
        print(f"Board saved to '{filename}'")
    except Exception as e:
        print(f"Error saving file: {e}")

def showBoard(PMineField: list[list[int]]) -> None:
    """Print the minefield row by row."""
    if not PMineField:
        print("No board generated yet.")
        return
    for row in PMineField:
        print(row)

# --- Main program ---
def main() -> None:
    print("Program starting.")
    MineField: list[list[int]] = []
    while True:
        showOptions()
        choice = askChoice()
        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            try:
                rows = int(input("Insert rows: "))
                cols = int(input("Insert columns: "))
                mines = int(input("Insert mines: "))
                if mines > rows * cols:
                    print("Too many mines for given field size.")
                    continue
                generateMinefield(MineField, rows, cols, mines)
                print("Minefield generated successfully.")
            except ValueError:
                print("Invalid input. Please insert integer values.")
        elif choice == 2:
            showBoard(MineField)
        elif choice == 3:
            saveBoard(MineField)
        else:
            print("Unknown option!")
        print("")
    print("Program ending.")

if __name__ == "__main__":
    main()
