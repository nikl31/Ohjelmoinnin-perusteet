########################################################
# Task A10_T3
# Developer First_name Last_name
# Date YYYY-MM-DD
########################################################

import sys
from typing import List

def bubbleSort(PValues: List[int], PAsc: bool = True) -> None:
    """Sorts the list PValues in-place using bubble sort algorithm.
    PAsc=True sorts ascending, False sorts descending.
    """
    n = len(PValues)
    for i in range(n - 1):  
        for j in range(n - i - 1):  
            if (PAsc and PValues[j] > PValues[j + 1]) or \
               (not PAsc and PValues[j] < PValues[j + 1]):
                PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]

def readValues(PFilename: str) -> List[int]:
    """Reads integers from a file, ignoring empty lines."""
    Values: List[int] = []
    try:
        with open(PFilename, "r") as f:
            for line in f:
                line = line.strip()
                if line != "":
                    Values.append(int(line))
    except FileNotFoundError:
        print(f'Error! File "{PFilename}" not found.')
        sys.exit(1)
    except ValueError as e:
        print(f"Error converting line to integer: {e}")
        sys.exit(1)
    return Values

def main() -> None:
    print("Program starting.")

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ")

    Values = readValues(filename)

    print(f"Raw '{filename}' -> {', '.join(map(str, Values))}")

    bubbleSort(Values, PAsc=True)
    print(f"Ascending '{filename}' -> {', '.join(map(str, Values))}")

    bubbleSort(Values, PAsc=False)
    print(f"Descending '{filename}' -> {', '.join(map(str, Values))}")

    print("Program ending.")

if __name__ == "__main__":
    main()
