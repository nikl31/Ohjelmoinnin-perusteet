DELIMITER = ";"
WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturnday",
    "Sunday",
)

class TIMESTAMP:
    def __init__(self):
        self.weekday: str = ""
        self.hour: str = ""
        self.consumption: float = 0.0
        self.price: float = 0.0


class DAY_USAGE:
    def __init__(self):
        self.usage: float = 0.0
        self.cost: float = 0.0


def readFile(PFilename: str, PTimestamps: list[TIMESTAMP]) -> None:
    print(f'Reading file "{PFilename}".')

    PTimestamps.clear()

    with open(PFilename, "r", encoding="utf-8") as f:
        header_skipped = False

        for Line in f:
            if not header_skipped:
                header_skipped = True
                continue

            Row = Line.rstrip()
            if Row == "":
                continue

            Cols = Row.split(DELIMITER)

            ts = TIMESTAMP()
            ts.weekday = Cols[0]
            ts.hour = Cols[1]
            ts.consumption = float(Cols[2])
            ts.price = float(Cols[3])

            PTimestamps.append(ts)

            Cols.clear()


def analyseTimestamps(PTimestamps: list[TIMESTAMP], PHelper: list[DAY_USAGE], PResults: list[str]) -> None:
    print("Analysing timestamps.")

    PHelper.clear()
    PResults.clear()

    for _ in WEEKDAYS:
        PHelper.append(DAY_USAGE())

    for ts in PTimestamps:
        for i, day in enumerate(WEEKDAYS):
            if ts.weekday == day:
                PHelper[i].usage += ts.consumption
                PHelper[i].cost += ts.consumption * ts.price
                break

    PResults.append("### Electricity consumption summary ###")
    for i, day in enumerate(WEEKDAYS):
        usage = PHelper[i].usage
        cost = PHelper[i].cost
        PResults.append(f" - {day} usage {usage:.2f} kWh, cost {cost:.2f} €")
    PResults.append("### Electricity consumption summary ###")


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    for r in PResults:
        print(r)


def main() -> None:
    print("Program starting.")

    Timestamps: list[TIMESTAMP] = []
    Helper: list[DAY_USAGE] = []
    Results: list[str] = []

    filename = input("Insert filename: ")
    readFile(filename, Timestamps)

    analyseTimestamps(Timestamps, Helper, Results)
    displayResults(Results)

    print("Program ending.")


main()
