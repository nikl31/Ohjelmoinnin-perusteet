def process_comma_separated_integers():
    print("Program starting.")
    
    user_input = input("Insert comma separated integers: ")
    items = user_input.split(",")
    
    valid_integers = []
    
    for item in items:
        item = item.strip()
        try:
            num = int(item)
            valid_integers.append(num)
        except ValueError:
            print(f"Invalid value detected: '{item}'")
    
    if valid_integers:
        total_count = len(valid_integers)
        total_sum = sum(valid_integers)
        parity = "even" if total_sum % 2 == 0 else "odd"
        print(f"There are {total_count} integers in the list.")
        print(f"Sum of the integers is {total_sum} and it's {parity}")
    else:
        print("No valid integers to analyze.")
    
    print("Program ending.")

process_comma_separated_integers()
