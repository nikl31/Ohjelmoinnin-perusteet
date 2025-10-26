def main():
    print("Program starting.")
    print("This program can read a file.")
    filename = input("Insert filename: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(f'#### START "{filename}" ####')
            print(file.read(), end="")  # print file content without extra newlines
            print(f'\n#### END "{filename}" ####')
    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')

    print("Program ending.")


if __name__ == "__main__":
    main()