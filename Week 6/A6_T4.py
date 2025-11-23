print("Program starting.")
print("This program analyses a list of names from a file.")

filename = input("Insert filename to read: ")

try:
    print(f'Reading names from "{filename}".')
    names = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:              
                parts = line.split(";")
                for name in parts:
                    name = name.strip()
                    if name:
                        names.append(name)

    print("Analysing names...")

    if names:
        name_count = len(names)
        shortest_name_len = len(min(names, key=len))
        longest_name_len = len(max(names, key=len))
        average_len = sum(len(n) for n in names) / name_count

        report = (
            "#### REPORT BEGIN ####\n"
            f"Name count - {name_count}\n"
            f"Shortest name - {shortest_name_len} chars\n"
            f"Longest name - {longest_name_len} chars\n"
            f"Average name - {average_len:.2f} chars\n"
            "#### REPORT END ####"
        )

        print("Analysis complete!")
        print(report)
    else:
        print("No names found in the file.")

except FileNotFoundError:
    print(f'Error: The file "{filename}" does not exist.')
except Exception as e:
    print(f"An error occurred: {e}")
print("Program ending.")