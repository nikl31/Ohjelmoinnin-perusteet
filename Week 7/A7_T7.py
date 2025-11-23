ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def load_config(filename: str):
    Rotor1 = ""
    Rotor2 = ""
    Rotor3 = ""
    Reflector = ""

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("Rotor1:"):
                Rotor1 = line.split(":")[1].strip()
            elif line.startswith("Rotor2:"):
                Rotor2 = line.split(":")[1].strip()
            elif line.startswith("Rotor3:"):
                Rotor3 = line.split(":")[1].strip()
            elif line.startswith("Reflector:"):
                Reflector = line.split(":")[1].strip()

    return [Rotor1, Rotor2, Rotor3], Reflector


def rotate_positions(pos):
    pos[0] += 1
    if pos[0] >= 26:
        pos[0] = 0
        pos[1] += 1
        if pos[1] >= 26:
            pos[1] = 0
            pos[2] += 1
            if pos[2] >= 26:
                pos[2] = 0


def forward_pass(c, rotors, pos):
    idx = ALPHABET.index(c)
    for i in range(3):
        offset = (idx + pos[i]) % 26
        letter = rotors[i][offset]
        idx = ALPHABET.index(letter)
    return ALPHABET[idx]


def reflect(c, reflector):
    idx = ALPHABET.index(c)
    return reflector[idx]


def reverse_pass(c, rotors, pos):
    idx = ALPHABET.index(c)
    for i in reversed(range(3)):
        rotor = rotors[i]
        shifted = ALPHABET[(idx + pos[i]) % 26]
        r_index = rotor.index(shifted)
        idx = (r_index - pos[i]) % 26
    return ALPHABET[idx]


def scramble_letter(ch, rotors, reflector, positions):
    rotate_positions(positions)
    c = forward_pass(ch, rotors, positions)
    c = reflect(c, reflector)
    c = reverse_pass(c, rotors, positions)
    return c


def main():
    config = input("Insert config(filename): ")
    rotors, reflector = load_config(config)

    plugs = input("Insert plugs (y/n)?: ")
    if plugs.lower() == "y":
        print("Plugs not implemented in this version.")
    else:
        print("No extra plugs inserted.")

    print("Enigma initialized.\n")

    while True:
        row = input("Insert row (empty stops): ")
        if row == "":
            print("\nEnigma closing.")
            break

        positions = [0, 0, 0]  

        output = ""
        for ch in row:
            if ch not in ALPHABET:
                continue  
            illuminated = scramble_letter(ch, rotors, reflector, positions)
            print(f"Character \"{ch}\" illuminated as \"{illuminated}\"")
            output += illuminated

        print(f"Converted row - \"{output}\".\n")


main()
