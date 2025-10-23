print("Program starting.")
print("This is a program with simple menu where you can choose which operation the program performs.")
Name = input("Before the menu, please insert your name: ")
print("")
print("Options:")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")
choice = int(input("Your choice: "))
first = Name[0]
reverse = Name[::-1]
length = (len(Name))
if (choice == 1):
    print (f"Welcome {Name}!")
elif(choice == 2):
    print(f"Your name backwards is '{reverse}'.")
elif(choice == 3):
    print(f"Your name's first character is '{first}'.")
elif(choice == 4):
    print(f"Your name's length is '{length}'.")
elif(choice == 0):
    print("Exiting...")

else:
    print("Unknown option.")





