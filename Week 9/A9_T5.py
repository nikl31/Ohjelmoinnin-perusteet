########################################################
# Task A9_T5
# Developer First_name Last_name
# Date 2025-11-23
########################################################

def collectRGB() -> tuple[int, int, int]:
    r = int(input("Insert red: "))
    g = int(input("Insert green: "))
    b = int(input("Insert blue: "))
    
    for value in (r, g, b):
        if not (0 <= value <= 255):
            raise ValueError("RGB value out of range")
    
    return r, g, b

def main():
    print("Program starting.")
    try:
        r, g, b = collectRGB()
        print("RGB Details:")
        print(f"- Red {r}")
        print(f"- Green {g}")
        print(f"- Blue {b}")
        print(f"- Hex #{r:02x}{g:02x}{b:02x}")
    except Exception:
        print("Couldn't perform the designed task due to the invalid input values.")
    print("Program ending.")

if __name__ == "__main__":
    main()
