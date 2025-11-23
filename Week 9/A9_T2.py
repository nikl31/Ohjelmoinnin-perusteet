########################################################
# Task A9_T2
# Developer First_name Last_name
# Date 2025-11-23
########################################################


import sys

def main():
    print("Program starting.")
    code_input = input("Insert exit code(0-255): ")
    try:
        code = int(code_input)
        if 0 <= code <= 255:
            print("Clean exit")
            sys.exit(code)
        else:
            print("Error! Exit code must be between 0 and 255.")
    except ValueError:
        print(f"Error! '{code_input}' is not a valid integer.")

if __name__ == "__main__":
    main()
