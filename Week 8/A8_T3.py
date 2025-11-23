def readValues(filename: str) -> list[float]:
    values: list[float] = []

    try:
        with open(filename, "r") as file:
            for row in file:
                row = row.strip()
                if row == "":
                    continue
                values.append(float(row))
    except:
        print("Error reading file.")

    return values


def calcSum(values: list[float]) -> float:
    return round(sum(values), 1)


def calcAverage(values: list[float]) -> float:
    if len(values) == 0:
        return 0.0
    return round(sum(values) / len(values), 1)


def showOptions() -> None:
    print("Options:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")


def main() -> None:
    print("Program starting.")

    values: list[float] = []

    while True:
        showOptions()
        choice = int(input("Your choice: "))

        if choice == 0:
            print("Exiting program.\n")
            break

        elif choice == 1:   # Read file
            filename = input("Insert filename: ")
            values = readValues(filename)
            print()

        elif choice == 2:   # Amount
            print(f"Amount of values {len(values)}\n")

        elif choice == 3:   # Sum
            print(f"Sum of values {calcSum(values)}\n")

        elif choice == 4:   # Average
            print(f"Average of values {calcAverage(values)}\n")

        else:
            print("Invalid choice.\n")

    print("Program ending.")


if __name__ == "__main__":
    main()
