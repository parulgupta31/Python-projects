from random import randint

choice = ['rock', 'paper', 'scissor']
computer = choice[randint(0, 2)]


def yes_no():
    ques = input('wanna play again? ')
    if ques == 'y':
        rock_paper_game()
    elif ques == 'n':
        print('u quit the game. Well played.👏👏')
    else:
        print('plz enter y/n only.')
        yes_no()


def rock_paper_game():
    choice = ['rock', 'paper', 'scissor']
    computer = choice[randint(0, 2)]

    if ask == 'y':
        player = input('you choose ').lower()
        print('computer chose: ' + computer)
        if player == computer:
            print('draw')
            yes_no()
        elif player == 'rock' and computer == 'paper':
            print('computer won')
            yes_no()
        elif player == 'rock' and computer == 'scissor':
            print('player won')
            yes_no()

        elif player == 'scissor' and computer == 'paper':
            print('player won')
            yes_no()
        elif player == 'scissor' and computer == 'rock':
            print('computer won')
            yes_no()
        elif player == 'paper' and computer == 'scissor':
            print('computer won')
            yes_no()
        elif player == 'paper' and computer == 'rock':
            print('player won')
            yes_no()
        else:
            print('plz enter rock, paper or scissor only')
            yes_no()
    elif ask == 'n':
        print('you exit')


print('welcome to "Rock", "Paper", "Scissor" game 😊')
ask = input('want to play "Rock", "Paper", "Scissor" game.y/n  ')
rock_paper_game()
