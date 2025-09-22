print("Program starting.")
task1 =input("Insert a closed compound word: ")
reverse = task1[::-1]
print(f"The word you inserted is '{task1}' and in reverse it is '{reverse}'.")
length = (len(task1))
print(f"The inserted word length is {length}")
last = task1[-1]
print(f"Last character is '{last}'")
print("Take substring from the inserted word by inserting...")
first = int(input("1) Starting point: "))
second = int(input("2) Ending point: "))
third = int(input("3) Step size: "))
complete = task1[first:second:third]
print(f"The word '{task1}' sliced to the defined substring is '{complete}'.")
print("Program ending.")