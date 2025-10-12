def frameWord(PWord):
    frame_length = len(PWord) + 4
    print('*' * frame_length)
    print(f"* {PWord} *")
    print('*' * frame_length)


def main():
    print("Program starting.")
    print()
    PWord = input("Insert word: ")
    print()
    frameWord(PWord)
    print()
    print("Program ending.")


if __name__ == "__main__":
    main()
    
