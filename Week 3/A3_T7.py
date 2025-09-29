def main():
    print("Program starting.")
    print("Testing decision structures.")
    
    # Prompt user for integer input
    try:
        value = int(input("Insert an integer: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    
    # Show menu
    print("Options:")
    print("1 - In one multi-branched decision")
    print("2 - In multiple independent if-statements")
    print("0 - Exit")
    
    choice = input("Your choice: ").strip()
    
    if choice == "1":
        print("Using one multi-branched decision structure.")
        # Multi-branched decision (like if/elif/else chain)
        if value >= 400:
            value += 44
        elif value >= 200:
            value += 22
        elif value >= 100:
            value += 11
        print(f"Result is {value}")
    
    elif choice == "2":
        print("Using multiple independent if-statements.")
        # Independent decisions (all can apply)
        if value >= 400:
            value += 44
        if value >= 200:
            value += 22
        if value >= 100:
            value += 11
        print(f"Result is {value}")
    
    elif choice == "0":
        print("Exiting…")
    
    else:
        print("Unknown option.")
    
    print("\nProgram ending.")


if __name__ == "__main__":
    main()