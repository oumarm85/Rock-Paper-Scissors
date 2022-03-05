import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line
game_images = [rock, paper, scissors]
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))

if player_input >= 0 and player_input <= 2:
  print(game_images[player_input])
else:
  print("Wrong input, you lost!")

cpu_input = random.randint(0, 2)
print("The computer chose:")
print(game_images[cpu_input])

if player_input == cpu_input:
  print("It's a draw")
elif player_input == 0 and cpu_input == 1 :
    print("Computer wins, you loose!")
elif player_input == 0 and cpu_input == 2 :
    print("You WON!!")
elif player_input == 1 and cpu_input == 0 :
    print("You WON!!")
elif player_input == 1 and cpu_input == 2 :
    print("Computer wins, you loose!")
elif player_input == 2 and cpu_input == 0 :
    print("Computer wins, you loose!")
elif player_input == 2 and cpu_input == 1 :
    print("You WON!!")
