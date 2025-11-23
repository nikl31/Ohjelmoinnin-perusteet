########################################################
# Task A10_T5
# Developer First_name Last_name
# Date YYYY-MM-DD
########################################################

def recursiveFactorial(PNum: int) -> int:
    """Calculate factorial of PNum recursively."""
    if PNum <= 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)

def main() -> None:
    print("Program starting.")
    
    try:
        n = int(input("Insert factorial: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = recursiveFactorial(n)
            print(f"Factorial {n}!\n{n}! = {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
    
    print("Program ending.")

if __name__ == "__main__":
    main()
