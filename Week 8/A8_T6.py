def showMainMenu():
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")


def showUserMenu():
    print("User menu:")
    print("1 - View profile")
    print("2 - Change password (not implemented)")
    print("0 - Logout")


def userSession(PUser: list[str]):
    while True:
        showUserMenu()
        choice = input("Your choice: ")

        if choice == "0":
            print("Logging out.\n")
            return

        elif choice == "1":
            print(f"User ID: {PUser[0]}")
            print(f"Username: {PUser[1]}\n")

        elif choice == "2":
            print("Password change not implemented.\n")

        else:
            print("Invalid option.\n")

def main():
    print("Program starting.")

    while True:
        showMainMenu()
        choice = input("Your choice: ")

        if choice == "0":
            print("Exiting program.\n")
            break

        elif choice == "1":
            username = input("Insert username: ")
            password = input("Insert password: ")

            logged = loginUser(username, password)
            if logged is None:
                print("Login failed.\n")
            else:
                print(f"Welcome {logged[1]}!\n")
                userSession(logged)

        elif choice == "2":
            username = input("Insert username: ")
            password = input("Insert password: ")
            registerUser(username, password)
            print("User registration completed!\n")

        else:
            print("Invalid option.\n")

    print("Program ending.")


if __name__ == "__main__":
    main()
