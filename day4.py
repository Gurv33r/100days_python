import random
winner = 0
while not winner:
    user_choice = int(input('Rock = 1, Paper = 2, Scissors = 3: '))
    if user_choice in range(1, 4):
        if user_choice == 1:
            print('You chose rock')
        elif user_choice == 2:
            print('You chose paper')
        else:
            print('You chose scissors')
        comp_choice = random.randint(1, 3)
        if comp_choice == 1:
            print('Computer chose rock')
        elif comp_choice == 2:
            print('Computer chose paper')
        else:
            print('Computer chose scissors')
        if comp_choice == user_choice:
            print('TIE\n-----------------------------------------------\nTry again')
        else:
            winner = 1 if user_choice - comp_choice in (1, -2) else 2
    else:
        print('Enter 1, 2, or 3 for rock, paper, and scissors respectively')
print('WIN') if winner else print('LOSE')
