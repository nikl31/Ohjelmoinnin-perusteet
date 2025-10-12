def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")


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
            print(f"Current count - {count}")
        elif choice == 2:
            count += 1
        elif choice == 3:
            count = 0
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
    
    print("\nProgram ending.")


if __name__ == "__main__":
    main()
