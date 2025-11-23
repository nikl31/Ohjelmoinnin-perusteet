import time

def main():
    print("Program starting.")
    pause_duration = 0.0

    while True:
        print("Options:")
        print("1 - Set pause duration")
        print("2 - Activate pause")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            value = input("Insert pause duration (s): ")
            try:
                pause_duration = float(value)
            except ValueError:
                print("Invalid value, pause duration unchanged.\n")
                continue
            print()

        elif choice == "2":
            print(f"Pausing for {pause_duration} seconds.")
            time.sleep(pause_duration)
            print("Unpaused.\n")

        elif choice == "0":
            print("Exiting program.\n")
            break

        else:
            print("Invalid choice.\n")

    print("Program ending.")

if __name__ == "__main__":
    main()
