def main():
    print("Program starting.")
    print("This program can read a file.")
    
    Filename = input("Insert filename: ")
    
    try:
        with open(Filename, "r") as file:
            content = file.read()
        
        print(f'#### START "{Filename}" ####')
        print(content)
        print(f'#### END "{Filename}" ####')
    
    except FileNotFoundError:
        print(f'file "{Filename}" not found!')

    print("Program ending")

if __name__ == "__main__":
    main()