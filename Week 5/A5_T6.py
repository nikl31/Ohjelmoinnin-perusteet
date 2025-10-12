def showOptions():
    """Displays the available menu options."""
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")


def askChoice():
    """Prompts user for input and returns an integer choice."""
    choice = input("Your choice: ")
    if not choice.isnumeric():
        print("Unknown option!")
        return -1
    return int(choice)


def main():
    """Main program logic for the Tally Counter."""
    print("Program starting.")
    count = 0
    running = True

    while running:
        print()
        showOptions()
        choice = askChoice()

        if choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            count += 1
            print(f"Count increased. Current count - {count}")
        elif choice == 3:
            count = 0
            print("Count reset to 0.")
        elif choice == 0:
            print("Exiting program.")
            running = False
        elif choice != -1:
            print("Unknown option!")

    print("\nProgram ending.")


if __name__ == "__main__":
    main()
