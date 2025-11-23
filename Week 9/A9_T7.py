########################################################
# Task A9_T7
# Developer Your_Name
# Date 2025-11-23
########################################################

import sys
import os

def showHelp() -> None:
    """Display program usage."""
    print("Usage: python {} <source_file> <destination_file>".format(sys.argv[0]))


def copyFile(PSrcFile: str, PDstFile: str) -> None:
    """Copy the content of PSrcFile to PDstFile, prompt if destination exists."""
    Proceed = True
    if os.path.exists(PDstFile):
        ans = input(f'Destination file "{PDstFile}" exists. Overwrite? (y/n): ').strip().lower()
        if ans != "y":
            print("Copy aborted.")
            Proceed = False

    if Proceed:
        try:
            with open(PSrcFile, "r") as src, open(PDstFile, "w") as dst:
                for line in src:
                    dst.write(line)
            print(f'Copying file "{PSrcFile}" to "{PDstFile}".')
        except Exception as e:
            print(f"Error! Could not copy files. {e}")
            sys.exit(-1)


def main() -> None:
    print("Program starting.")

        print(f"Invalid amount of arguments: {len(sys.argv)}")
        showHelp()
        sys.exit(1)

    SrcFile = sys.argv[1]
    DstFile = sys.argv[2]

    print(f'Source file "{SrcFile}"')
    print(f'Destination file "{DstFile}"')

    if not os.path.exists(SrcFile):
        print(f'Error! Source file "{SrcFile}" does not exist.')
        sys.exit(-1)

    copyFile(SrcFile, DstFile)

    print("Program ending.")


if __name__ == "__main__":
    main()
