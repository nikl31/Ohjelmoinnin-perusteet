def insertWord():
    word = input("Insert word: ")
    return word

def showWord(word):
    print(f'Current word - "{word}"')

def showWordReversed(word):
    print(f'Word reversed - "{word[::-1]}"')

def main():
    print("Program starting.")
    current_word = ""
    
    while True:
        print("\nOptions:")
        print("1 - Insert word")
        print("2 - Show current word")
        print("3 - Show current word in reverse")
        print("0 - Exit")
        choice = input("Your choice: ")
        
        if choice == "1":
            current_word = insertWord()
        elif choice == "2":
            showWord(current_word)
        elif choice == "3":
            showWordReversed(current_word)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option")
    
    print("\nProgram ending.")

if __name__ == "__main__":
    main()
