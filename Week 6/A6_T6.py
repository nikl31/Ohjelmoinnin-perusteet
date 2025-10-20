LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rot13(text):
    result = ""
    for char in text:
        if char.islower():
            index = LOWER_ALPHABETS.find(char)
            result += LOWER_ALPHABETS[(index + 13) % 26]
        elif char.isupper():
            index = UPPER_ALPHABETS.find(char)
            result += UPPER_ALPHABETS[(index + 13) % 26]
        else:
            result += char
    return result

def main():
    print("Program starting.\n")
    rows = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        rows.append(row)
    
    ciphered_rows = [rot13(r) for r in rows]
    
    print("\n#### Ciphered text ####")
    for r in ciphered_rows:
        print(r)
    
    print("\n#### Ciphered text ####")
    save_file = input("Insert filename to save: ")
    
    with open(save_file, 'w', encoding='utf-8') as f:
        for r in ciphered_rows:
            f.write(r + "\n")
    
    print("Ciphered text saved!")
    print("Program ending.")

if __name__ == "__main__":
    main()
