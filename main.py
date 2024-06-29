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

#Write your code below this line 👇
import random
Choice= input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
Ans=int(Choice)

print("\nYou Chose")
if Ans==0:
    print(rock)
    print("rock")
elif Ans==1:
    print(paper)
    print("paper")
else:
    print(scissors)
    print("scissors")

print("\nComputer Chose")
computer_choice=random.randint(0,2)
if computer_choice==0:
    print(rock)
    print("rock")
elif computer_choice==1:
    print(paper)
    print("paper")
else:
    print(scissors)
    print("scissors")

if computer_choice==0 and Ans==0 or  computer_choice==1 and Ans==1 or computer_choice==2 and Ans==2:
    print("\nTry Again")
elif Ans==0 and computer_choice==2 or Ans==1 and computer_choice==0 or Ans==2 and computer_choice==1:
    print("\nYou Win!!!! :)")
else:
    print("\nYou lost:(")