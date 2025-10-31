DELIMITER = ',' \

def collectWords():
    words =[]

    while True:
        word = input("Insert word(empty stops): ").strip()

        if word == "":
            break

        words.append(word)

    return DELIMITER.join(word)




def options():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    
def askChoice():
    choice = input("Your choice: ").strip()
    if choice.isnumeric():
        return int(choice)
    
    else:
        return -1
        
def main():
    count = 0
    print("Program starting.")
    
    while True:
        options()
        choice = askChoice()
        
        if choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            count += 1
            print(f"Count increased!")
        elif choice == 3:
            count = 0
            print ("Count reset to 0")
        elif choice == 0:
            print("Exiting program.")
            print("\nProgram ending.")
            break
        
        else:
            print("Unknown option!")
            
if __name__ == "__main__":
    main()

