########################################################
# Task A9_T6
# Developer First_name Last_name
# Date 2025-11-23
########################################################

def showOptions() -> None:
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return -1

def saveLines(PLines: list[str]) -> None:
    if not PLines:
        print("No lines to save.\n")
        return
    try:
        filename = input("Insert filename: ")
        with open(filename, "w", encoding="utf-8") as f:
            for line in PLines:
                f.write(line + "\n")
        print(f"Lines saved to '{filename}'\n")
    except Exception as e:
        print(f"Error saving file: {e}")

def insertLine(PLines: list[str]) -> None:
    try:
        text = input("Insert text: ")
        PLines.append(text)
    except Exception as e:
        print(f"Error inserting line: {e}")

def onInterrupt(PLines: list[str]) -> None:
    print("\nKeyboard interrupt and unsaved progress!")
    if PLines:
        try:
            save_choice = input("Save before quit(y/n)?: ").strip().lower()
            if save_choice == "y":
                saveLines(PLines)
        except Exception:
            print("Error during saving.")
    print("Program ending.")

def main() -> None:
    Lines: list[str] = []
    Choice = -1
    print("Program starting.")
    try:
        while Choice != 0:
            showOptions()
            Choice = askChoice()
            if Choice == 1:
                insertLine(Lines)
            elif Choice == 2:
                saveLines(Lines)
            elif Choice == 0:
                if Lines:
                    save_choice = input("You have unsaved lines. Save before exit(y/n)?: ").strip().lower()
                    if save_choice == "y":
                        saveLines(Lines)
                print("Exiting program.\n")
            else:
                print("Unknown option!\n")
    except KeyboardInterrupt:
        onInterrupt(Lines)
    Lines.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()

