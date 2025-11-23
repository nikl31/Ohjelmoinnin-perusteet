########################################################
# Task A9_T4
# Developer First_name Last_name
# Date 2025-11-23
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius() -> float:
    feed = input("Insert Celsius: ")
    try:
        celsius = float(feed)
    except ValueError:
        raise ValueError(f"could not convert string to float: '{feed}'")
    
    if not (TEMP_MIN <= celsius <= TEMP_MAX):
        raise Exception(f"{celsius} temperature out of range.")
    
    return celsius

def main():
    print("Program starting.")
    try:
        celsius = collectCelsius()
        print(f"You inserted {celsius} °C")
    except Exception as e:
        print(f"Error! {e}")
    print("Program ending.")

if __name__ == "__main__":
    main()
