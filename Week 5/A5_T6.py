def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

def askChoice():
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    else:
        return -1

def main():
    print("Program starting.")
    
    count = 0
    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            print(f"Current count - {count}\n")
        elif choice == 2:
            count += 1
            print(f"Count increased to {count}\n")
        elif choice == 3:
            count = 0
            print("Count reset to 0\n")
        elif choice == 0:
            print("Exiting program.\n")
            break
        else:
            print("Unknown option!\n")

    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
