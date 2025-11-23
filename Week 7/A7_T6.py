import random
random.seed(1234)

# ASCII ART
ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def print_art(choice: int) -> None:
    if choice == 1:
        print(ROCK)
    elif choice == 2:
        print(PAPER)
    elif choice == 3:
        print(SCISSORS)


def get_choice_name(choice: int) -> str:
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"


def determine_winner(p: int, b: int, player: str, bot: str) -> str:
    if p == b:
        return f"Draw! Both players chose {get_choice_name(p)}."

    # Rock(1) beats Scissors(3)
    if p == 1 and b == 3:
        return f"{player} rock beats {bot} scissors."
    if b == 1 and p == 3:
        return f"{bot} rock beats {player} scissors."

    # Paper(2) beats Rock(1)
    if p == 2 and b == 1:
        return f"{player} paper beats {bot} rock."
    if b == 2 and p == 1:
        return f"{bot} paper beats {player} rock."

    # Scissors(3) beat Paper(2)
    if p == 3 and b == 2:
        return f"{player} scissors beats {bot} paper."
    if b == 3 and p == 2:
        return f"{bot} scissors beats {player} paper."


def main() -> None:
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")

    player = input("Insert player name: ")
    bot = "RPS-3PO"

    print(f"Welcome {player}!")
    print(f"Your opponent is {bot}.")
    print("Game starts...\n")

    # Stats
    p_wins = 0
    p_losses = 0
    draws = 0

    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")

        try:
            choice = int(input("Your choice: "))
        except ValueError:
            print("Invalid input.\n")
            continue

        if choice == 0:
            print("\nResults:")
            print(f"{player} - wins ({p_wins}), losses ({p_losses}), draws ({draws})")
            print(f"{bot} - wins ({p_losses}), losses ({p_wins}), draws ({draws})")
            print("\nProgram ending.")
            return

        if choice not in (1, 2, 3):
            print("Invalid option.\n")
            continue

        bot_choice = random.randint(1, 3)

        print("Rock! Paper! Scissors! Shoot!\n")
        print("#########################")
        print(f"{player} chose {get_choice_name(choice)}.\n")
        print_art(choice)
        print("#########################")
        print(f"{bot} chose {get_choice_name(bot_choice)}.\n")
        print_art(bot_choice)
        print("#########################\n")

        result = determine_winner(choice, bot_choice, player, bot)

        # Count stats
        if "Draw!" in result:
            draws += 1
        elif result.startswith(player):
            p_wins += 1
        else:
            p_losses += 1

        print(result + "\n")


main()
