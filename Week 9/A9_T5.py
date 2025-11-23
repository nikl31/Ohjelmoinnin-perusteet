########################################################
# Task A9_T5
# Developer First_name Last_name
# Date 2025-11-23
########################################################

def askIntByte(PPrompt: str) -> int:
    Feed = input(PPrompt)
    try:
        value_float = float(Feed)
        value_int = int(value_float)
        if value_float != value_int:
            raise ValueError(f"{Feed} is not an integer")
        if not (0 <= value_int <= 255):
            raise ValueError(f"{Feed} out of range")
        return value_int
    except ValueError as ve:
        raise ve

def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(PRed, PGreen, PBlue)

def main():
    print("Program starting.")
    try:
        red = askIntByte("Insert red: ")
        green = askIntByte("Insert green: ")
        blue = askIntByte("Insert blue: ")

        hex_color = createHex(red, green, blue)

        print("RGB Details:")
        print(f"- Red {red}")
        print(f"- Green {green}")
        print(f"- Blue {blue}")
        print(f"- Hex {hex_color}")
        print(f"- R-byte {red:08b}")
        print(f"- G-byte {green:08b}")
        print(f"- B-byte {blue:08b}")

    except Exception:
        print("Couldn't perform the designed task due to the invalid input values.")
    
    print("Program ending.")

if __name__ == "__main__":
    main()
