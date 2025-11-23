########################################################
# Task A9_T1
# Developer First_name Last_name
# Date 2025-11-23
########################################################

def main():
    print("Program starting.\n")
    total = 0.0

    while True:
        value = input("Insert a floating-point value (0 to stop): ")
        if value == "0":
            break
        try:
            fvalue = float(value)
            total += fvalue
        except ValueError:
            print("Error! '{}' couldn't be converted to float.".format(value))

    print("\nFinal sum is {:.2f}".format(total))
    print("Program ending.")

if __name__ == "__main__":
    main()
