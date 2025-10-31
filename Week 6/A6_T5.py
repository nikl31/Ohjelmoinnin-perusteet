SEPARATOR = ";"

def readValues(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as file:
        values = ""
        for line in file:
            number = int(line.strip())
            values += str(number) + SEPARATOR
        values = values.rstrip(SEPARATOR)
    return values

def analyseNumbers(values: str) -> str:
    nums = [int(x) for x in values.split(SEPARATOR)]
    total = sum(nums)
    count = len(nums)
    greatest = max(nums)
    average = total / count
    return f"{count}{SEPARATOR}{total}{SEPARATOR}{greatest}{SEPARATOR}{average:.2f}"

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print("Count;Sum;Greatest;Average")
    
    try:
        values = readValues(filename)
        results = analyseNumbers(values)
        print(results)
    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n#### Number analysis - END ####")
    print("Program ending.")

if __name__ == "__main__":
    main()
