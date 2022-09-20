from random import randint

choice = [5]
computer = randint(0,9)




def display_board(board):
    current_status =[5]
    current_status.append(board)
    print(current_status)
    # and prints it out to the console.


def users_input():
    position_filled = [5]
    user_input = int(input("enter ur move "))
    if 0 < user_input < 10:
        if user_input not in position_filled:
            position_filled.append(user_input)
        else:
            user_input = int(input("enter ur move again  "))
            users_input(user_input)
    else:
        print("please enter in between 0 to 10 only")
        users_input(user_input)