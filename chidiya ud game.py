from random import randint


def chidiya_game():
    chidiya_ud_game = [['crow', 'peacock', 'duck'], ['tiger', 'lion', 'cheetah']]
    fly_nonfly = chidiya_ud_game[randint(0, 1)]
    computer_choose = fly_nonfly[randint(0, 2)]
    print('computer_choose:  ' + computer_choose)

    if fly_nonfly == chidiya_ud_game[0]:
        player = input('is ' + computer_choose.upper() + ' flying object? select yes  and pass please ')
        if player == 'pass':
            print('u  passed this.')

            yes_no()
        elif player == 'yes':
            print('u r correct.')

            yes_no()
        else:
            print('choose pass or yes only.')
            yes_no()
    elif fly_nonfly == chidiya_ud_game[1]:
        player = input('is ' + computer_choose.upper() + ' flying object? select yes or pass.  ')

        if player == 'pass':
            print('u passed it.')
            wanan

            yes_no()
        elif player == 'yes':
            print('u r wrong.')

            yes_no()
        else:
            print('choose between pass and yes only.')
            yes_no()


def yes_no():
    ques = input('wanna play again? ')
    if ques == 'y' or 'yes':
        chidiya_game()
    elif ques == 'n' or 'no':
        print('u quit the game. Well played.👏👏')
    else:
        print("plz enter yes or no only.")
    yes_no()





print('lets play chidiya ud game.yes or pass.😊  ')
chidiya_game()
