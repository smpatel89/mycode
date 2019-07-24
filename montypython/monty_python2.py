#!/usr/bin/env python3
round = 0
while(True):
    round += 1
    print('Finish the movie title, "Monty Python\'s The Life of ______')
    answer = input()
    if answer.lower() == 'brian' or answer.upper() == 'BRIAN':
        print('Correct')
        break
    if answer.lower() == 'shrubbery' or answer.upper() == 'SHRUBBERY':
        print('You gave the super secret answer!')
        break
    elif round == 3:
        print('Sorry, the answer was Brian')
        break
    else:
        print('Sorry! Try again')
