########################################################
# Task A10_T2
# Developer First_name Last_name
# Date YYYY-MM-DD
########################################################

import sys
from functools import reduce
from operator import mul

def readValues(PFilename: str, PValues: list[int]) -> None:
    """Reads integers from a file, ignoring empty lines, and fills PValues list."""
    try:
        with open(PFilename, "r") as f:
            for line in f:
                line = line.strip()
                if line != "":
                    try:
                        value = int(line)
                        PValues.append(value)
                    except ValueError:
                        print(f"Warning: '{line}' is not an integer, skipping.")
    except FileNotFoundError:
        print(f'Error! File "{PFilename}" not found.')
        sys.exit(1)

def sumOfValues(PValues: list[int]) -> int:
    """Returns the sum of all integers in PValues."""
    return sum(PValues)

def productOfValues(PValues: list[int]) -> int:
    """Returns the product of all integers in PValues."""
    if not PValues:
        return 0
    return reduce(mul, PValues, 1)

def main() -> None:
    Values: list[int] = []
    print("Program starting.")
    filename = input("Insert filename: ")
    readValues(filename, Values)

    print("# --- Sum of numbers --- #")
    print(sumOfValues(Values))
    print("# --- Sum of numbers --- #")

    print("# --- Product of numbers --- #")
    print(productOfValues(Values))
    print("# --- Product of numbers --- #")
    
    Values.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()
