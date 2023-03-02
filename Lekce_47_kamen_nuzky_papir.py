

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

# vytvoření listu pro kámen, nůžky, papír
list_vyberu = [rock, paper, scissors]

# proměnna pro obrazek - uživatel, vybrat index, který se rovná v user_choice a v obrázcích se mi ukáže konkrétní obrázek volby
user_picture = list_vyberu[user_choice]

# proměnná pro obázek - počítač
user_computer = list_vyberu[computer_choice]

# vyprintování
print(f"Uživatel si vybral:\n {user_picture}")
print(f"Počítač si vybral:\n {user_computer}")

# pravidla hry


if user_choice == computer_choice:
    print("Remíza")
elif user_choice == 0 and computer_choice == 1:
    print("Prohrál jsi, počítač vyhrává")
elif user_choice == 0 and computer_choice == 2:
    print("Vyhrál jsi, počítač prohrává")
elif user_choice == 1 and computer_choice == 0:
    print("Vyhrál jsi, počítač prohrává")
elif user_choice == 1 and computer_choice == 2:
    print("Prohrál jsi, počítač vyhrává")
elif user_choice == 2 and computer_choice == 0:
    print("Prohrál jsi, počítač vyhrává")
elif user_choice == 2 and computer_choice == 1:
    print("Vyhrál jsi, počítač prohrává")
