def even_odd(x):
    if x == 'yes' or x == 'no':
        print('plz enter numbers only.')
        y = input('wanna play? ')
        yes_no(y)
    elif int(x) % 2 == 0:
        print('its an EVEN number.Have another?')
        z = input('play again?  ')
        yes_no(z)
    if int(x) % 2 != 0:
        print('its an ODD number.Have another?')
        z = input('play again?  ')
        yes_no(z)
    else:
        print("exit")


def yes_no(z):
    if z.lower() == 'yes':
        y = input('type another?  ')
        even_odd(y)
    if z.lower() == 'no':
        print('u exit.')
    else:
        print('plz enter yes or no only.')
        v = input('play again? ')
        yes_no(v)


# odd or even
print("welcome to odd and even game")
print('type exit if  want to quit.')
y = input('do u want to play evn or odd game.yes/no ')

if y.lower() == 'yes':
    x = input('enter the number   ')
    even_odd(x)
if y.lower() == 'no':
    print('u exit')
