WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

def readFile(PFilename: str, PRows: list[str]) -> None:
    print(f'Reading file "{PFilename}".')
    PRows.clear()

    try:
        with open(PFilename, "r", encoding="utf-8") as f:
            first = True
            for line in f:
                if first:
                    first = False
                    continue  

                line = line.strip()
                if line == "":
                    continue  

                PRows.append(line)
    except FileNotFoundError:
        print(f'Error: File "{PFilename}" not found.')
    return None


def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    PResults.clear()

    WeekdayTimestampAmount: list[int] = [0] * 7

    for row in PRows:
        for i, day in enumerate(WEEKDAYS):
            if row.startswith(day):
                WeekdayTimestampAmount[i] += 1

    PResults.append("### Timestamp analysis ###")
    for i, day in enumerate(WEEKDAYS):
        PResults.append(f" - {day} {WeekdayTimestampAmount[i]} stamps")
    PResults.append("### Timestamp analysis ###")

    return None


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    for line in PResults:
        print(line)
    return None


def main() -> None:
    print("Program starting.")

    rows: list[str] = []
    results: list[str] = []

    filename = input("Insert filename: ")

    readFile(filename, rows)
    analyseTimestamps(rows, results)
    displayResults(results)

    rows.clear()
    results.clear()

    print("Program ending.")
    return None

if __name__ == "__main__":
       main()

