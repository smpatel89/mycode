#!/usr/bin/env python3

''' Main function '''

def main_function():
    ''' Main function '''
    pets_list = [2, 'cats', 3, 'dogs']

    print(f'I have {pets_list[2]} {pets_list[1]} and {pets_list[0]} {pets_list[3]}.')
    print('I have {} {} and {} {}.'.format(pets_list[2], pets_list[1], pets_list[0], pets_list[3]))
    print('I have {2} {1} and {0} {3}.'.format(*pets_list))

main_function()
