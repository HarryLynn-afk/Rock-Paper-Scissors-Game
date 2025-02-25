import random
#Games images
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

user_answer = input("What do you choose? Type 0 for Rock,"
                    "1 for Paper or 2 for Scissors\n")
user_answer_check = ["0","1","2"]
while user_answer not in user_answer_check:
    print("Invalid answer! Please type 0 or 1 or 2")
    user_answer = input("What do you choose? Type 0 for Rock,"
                    "1 for Paper or 2 for Scissors\n")

user_answer = int(user_answer)

game_images = [rock, paper, scissors]

print("YOUR CHOSE:")
print(game_images[user_answer])

print("COMPUTER CHOSE:")
computer_chose = random.randint(0,2)
print(game_images[computer_chose])

if user_answer == computer_chose:
    print("It's a draw.")

elif (user_answer == 0 and computer_chose == 2) or \
     (user_answer == 1 and computer_chose == 0) or \
     (user_answer == 2 and computer_chose == 1):
    print("You Win!")
else:
    print("You Lose!")



