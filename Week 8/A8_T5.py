from loginLib import login, register, viewProfile, change_password

def main() -> None:
    print("Program starting.")
    mainMenu()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")

def showUserMenu() -> None:
    print("User menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")

def mainMenu() -> None:
    while True:
        showOptions()
        try:
            choice = askChoice()
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            username = askValue("username")
            password = askValue("password")
            if login(username, password):
                print(f"Welcome {username}!\n")
                userMenu(username)
            else:
                print("Login failed.\n")
        elif choice == 2:
            username = askValue("username")
            password = askValue("password")
            register(username, password)
            print("User registration completed!\n")
        else:
            print("Invalid option.\n")

def userMenu(PUsername: str) -> None:
    while True:
        showUserMenu()
        try:
            choice = askChoice()
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if choice == 0:
            print("Logging out.\n")
            break
        elif choice == 1:
            viewProfile(PUsername)
        elif choice == 2:
            change_password(PUsername)
        else:
            print("Invalid option.\n")

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue(PPrompt: str) -> str:
    return input(f"Insert {PPrompt}: ")

if __name__ == "__main__":
    main()
