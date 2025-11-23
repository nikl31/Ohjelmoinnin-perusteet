DELIMITER = ";"


class TIMESTAMP:
    def __init__(self):
        self.weekday: str = ""
        self.hour: str = ""
        self.consumption: float = 0.0
        self.price: float = 0.0


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

            Columns = Row.split(DELIMITER)
            ts = TIMESTAMP()

            ts.weekday = Columns[0]
            ts.hour = Columns[1]
            ts.consumption = float(Columns[2])
            ts.price = float(Columns[3])

            PTimestamps.append(ts)
            Columns.clear()


def displayTimestamps(PTimestamps: list[TIMESTAMP]) -> None:
    print("Electricity usage:")
    for ts in PTimestamps:
        total = ts.consumption * ts.price
        print(
            f" - {ts.weekday} {ts.hour}, price {ts.price:.2f}, "
            f"consumption {ts.consumption:.2f} kWh, total {total:.2f} €"
        )


def main() -> None:
    print("Program starting.")

    Timestamps: list[TIMESTAMP] = []

    filename = input("Insert filename: ")
    readFile(filename, Timestamps)

    displayTimestamps(Timestamps)

    print("Program ending.")

if __name__ == "__main__":
       main()

