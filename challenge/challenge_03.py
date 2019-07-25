#!/usr/bin/env python3

example_list = ['banana', 'blueberries', 'nuts', 'acorns']

def examine_list(list):
    short_cutoff = 5
    med_cutoff = 10

    list_short = []
    list_med = []
    list_long = []

    for item in list:
        if len(item) < short_cutoff:
            list_short.append(item)
        if len(item) < med_cutoff:
            list_med.append(item)
        if len(item) >= med_cutoff:
            list_long.append(item)

    print(f'{len(list_short)} Short items')
    print(f'{len(list_med)} Medium items')
    print(f'{len(list_long)} Long items')

def main():
    f = open('list_items.txt', 'r')
    item_array = []
    for line in f:
        item_array.append(line)
    examine_list(item_array)
    f.close()

main()
    
