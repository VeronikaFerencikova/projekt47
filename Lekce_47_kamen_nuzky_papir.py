

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

import random
# uživatel zadá výběr - kámen 0, nůžky 2, papír 1

user_choice = int(input("Co si vyberete? Napište 0 pokud kámen, 1 pokud papír, 2 pokud nůžky\n"))
# print(user_choice)

# počítač vybírá volby - kámen 0, papír 1, nůžky 2 - stejná volba
computer_choice = random.randint(0, 2)
# print(computer_choice)