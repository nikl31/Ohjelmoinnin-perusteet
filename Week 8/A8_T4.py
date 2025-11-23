def showOptions() -> None:
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")


def main() -> None:
    print("Program starting.")

    filename = input("Insert filename: ")
    timestamps = []
    readTimestamps(filename, timestamps)

    while True:
        showOptions()
        choice = int(input("Your choice: "))

        if choice == 0:
            print("Exiting program.\n")
            break

        elif choice == 1:
            year = int(input("Insert year: "))
            amount = calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {amount}\n")

        elif choice == 2:
            month = input("Insert month: ")
            if month not in MONTHS:
                print("Invalid month.\n")
                continue
            amount = calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {amount}\n")

        elif choice == 3:
            weekday = input("Insert weekday: ")
            if weekday not in WEEKDAYS:
                print("Invalid weekday.\n")
                continue
            amount = calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {amount}\n")

        else:
            print("Invalid option.\n")

    print("Program ending.")


if __name__ == "__main__":
    main()
