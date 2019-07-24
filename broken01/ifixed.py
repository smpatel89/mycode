#!/usr/bin/env python3
calc1 = 0.0
calc2 = 0.0
operation = ''
while (calc1 != 'q'):
    print('\nWhat is the first operator? Or enter q to quit ')
    calc1 = input()
    if calc1 == 'Q':
        break
    calc1 = float(calc1)
    print('\nWhat is the second operaator? Or enter q to quit ')
    calc2 = input()
    if calc2 == 'Q':
        break
    calc2 = float(calc2)
    print('Enter an operator to perform. Either + or -: ')
    operation = input()
    if operation == '+':
        print(f'\n {str(calc1)} + {str(calc2)} = {str(calc1 + calc2)}')
    elif operation == '--': 
        print(f'\n {str(calc1)} + {str(calc2)} = {str(calc1 + calc2)}')
    else:
        print('\nNot valid')
