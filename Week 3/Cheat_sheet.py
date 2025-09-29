name1 = input("eka nimi: ")
name2 = input("toka nimi: ")
if len(name1) > len(name2):
    print("eka nimi pidempi")
elif len(name1) < len(name2):
    print("toka nimi pidempi")
else:
    print("saman mittaisia")

Town = "Kouvola"
Street = "Ahventie" 
Building = 1

if(Town is "Kouvola" and Street is "Ahventie" and Building is 1):
  print("You are at home")
elif not(Town is "Kouvola" and Street is "Ahventie" and Building is 1):
  print("You are lost...")

import random
choices = ["Kivi", "Sakset", "Paperi"]
computer_choice = random.choice(choices)
player_choice = input("Your choice: ")
elif (player_choice is "Kivi"and computer_choice is "Sakset") or \ 
(player_choice is "Sakset" and computer_choice is "Paperi") or \ 
(player_choice is "Paperi"and computer_choice is "Kivi"):
print("Pelaaja voittaa!")
else
print("Tietokone voittaa!")

  
