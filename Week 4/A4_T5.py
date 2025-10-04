print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))

valid = True

if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    valid = False

if inspection < start or inspection > stop:
    print("Inspection value must be within the range of start and stop.")
    valid = False

if valid:
    print("\nFirst loop - inspection with break:")
    for i in range(start, stop):
        if i == inspection:
            break
        if i < inspection - 1:
            print(i, end=" ")
        else:
            print(i)

    print("")

    print("Second loop - inspection with continue:")
    for i in range(start, stop):
        if i == inspection:
            continue
        if (i == stop - 1) or (i == inspection + 1 and stop == inspection + 2):
            print(i)
        elif i == stop - 1:
            print(i)
        elif i == stop - 2 and inspection == stop - 1:
            print(i)
        elif i == stop - 1:
            print(i)
        elif i == stop - 1:
            print(i)
        elif i == stop - 1:
            print(i)
        elif i == stop - 1:
            print(i)
        else:
            if i < stop - 1:
                if i != inspection and (i < stop - 2 or inspection == stop - 1):
                    print(i, end=" ")
                elif i == stop - 1:
                    print(i)
            else:
                print(i)

print("\nProgram ending.")
