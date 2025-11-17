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
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("You did't select yet")
print("Computer chose:")
pc_choice = random.randint(0,2)
if choice >= 3 or choice<0:
    print("-")
elif pc_choice == 0:
    print(rock)
elif pc_choice == 1:
    print(paper)
else:
    print(scissors)

if choice == 0 and pc_choice == 1:
    print("You lost")
elif choice == 0 and pc_choice == 2:
    print("You Win")
elif choice == 1 and pc_choice == 2:
    print("You lost")
elif choice == 1 and pc_choice == 0:
    print("You Win")
elif choice == 2 and pc_choice == 0:
    print("You lost")
elif choice == 2 and pc_choice == 1:
    print("You Win")
elif choice == pc_choice:
    print("It’s a tie!")