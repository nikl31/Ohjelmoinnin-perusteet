LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rot13(text):
    result = []
    for char in text:
        if char in LOWER_ALPHABETS:
            index = LOWER_ALPHABETS.index(char)
            result.append(LOWER_ALPHABETS[(index + 13) % 26])
        elif char in UPPER_ALPHABETS:
            index = UPPER_ALPHABETS.index(char)
            result.append(UPPER_ALPHABETS[(index + 13) % 26])
        else:
            result.append(char)
    return ''.join(result)

def main():
    print("Program starting.\n")
    print("Collecting plain text rows for ciphering.")
    lines = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        lines.append(row)

    ciphered_lines = [rot13(line) for line in lines]

    print("\n#### Ciphered text ####")
    for line in ciphered_lines:
        print(line)

    print("\n#### Ciphered text ####")
    filename = input("Insert filename to save (leave empty to just show): ")

    if filename.strip():
        with open(filename, "w", encoding="utf-8") as f:
            for line in ciphered_lines:
                f.write(line + "\n")
        print("Ciphered text saved!")
    else:
        print("No file saved.")

    print("Program ending.")

if __name__ == "__main__":
    main()