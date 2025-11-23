########################################################
# Task A10_T4
# Developer First_name Last_name
# Date YYYY-MM-DD
########################################################

import sys
from typing import List

def merge(PLeft: List[int], PRight: List[int], PMerge: List[int], PAsc: bool = True) -> None:
    """Merge two sorted lists PLeft and PRight into PMerge in-place."""
    i = j = k = 0
    while i < len(PLeft) and j < len(PRight):
        if (PAsc and PLeft[i] <= PRight[j]) or (not PAsc and PLeft[i] >= PRight[j]):
            PMerge[k] = PLeft[i]
            i += 1
        else:
            PMerge[k] = PRight[j]
            j += 1
        k += 1

    while i < len(PLeft):
        PMerge[k] = PLeft[i]
        i += 1
        k += 1
    while j < len(PRight):
        PMerge[k] = PRight[j]
        j += 1
        k += 1

def mergeSort(PValues: List[int], PAsc: bool = True) -> None:
    """Sort PValues using merge sort algorithm."""
    if len(PValues) <= 1:
        return
    mid = len(PValues) // 2
    left = PValues[:mid]
    right = PValues[mid:]
    mergeSort(left, PAsc)
    mergeSort(right, PAsc)
    merge(left, right, PValues, PAsc)

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

    mergeSort(Values, PAsc=True)
    print(f"Ascending '{filename}' -> {', '.join(map(str, Values))}")

    mergeSort(Values, PAsc=False)
    print(f"Descending '{filename}' -> {', '.join(map(str, Values))}")

    print("Program ending.")

if __name__ == "__main__":
    main()
