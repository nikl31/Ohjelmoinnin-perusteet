########################################################
# Task A9_T3
# Developer First_name Last_name
# Date 2025-11-23
########################################################

import sys
import os

def main():
    print("Program starting.")
    filename = input("Insert filename: ")

    if not os.path.exists(filename):
        print(f"Error! File '{filename}' does not exist.")
        sys.exit(1)

    print(f"## {filename} ##")
    try:
        with open(filename, "r") as file:
            for line in file:
                print(line.rstrip())
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    print(f"## {filename} ##")

    print("Program ending.")

if __name__ == "__main__":
    main()
