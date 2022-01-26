def main():
    begin = input("Begin your adventure by choosing from 3 areas: the beach (1), the woods (2), or a castle (3) - ")
    if int(begin) == 1:
        print('''You chose the beach!
You are walking along the shore and suddenly see a glass bottle sticking out of sand.''')
        chose_bottle = input('Do you pick it up (Y/N)? - ').upper() == 'Y'
        if chose_bottle:
            print('''You pull the glass bottle out of the sand and see a rolled-up slip of paper in it.
You open the bottle and pull out the slip. It says, 
    \'If you are reading this, you are worthy of my treasure. 
    Seek out the last place you would look.\'
You decide to look around nearby for this \'treasure\' and eventually you find it a couple of feet away, hidden under some washed-up kelp.''')
            print('You win! :)')
        else:
            print('You decide to keep walking along the beach and live a long life, free of treasure')
            print('you lose :(')
            return
    elif int(begin) == 2:
        print('You have chosen the woods and die from mosquito bites')
        print('You lose :(')
        return
    elif int(begin) == 3 :
        print('You have chosen the castle and die from rogue knights')
        print('You lose :(')
        return
    else:
        print('You have chosen none of those and die from varying off the path')
        print('You lose :(')
        return
    
main()