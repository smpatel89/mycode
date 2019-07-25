#!/usr/bin/env python3
## create file object in "r"ead mode
print('Name of config to read? ')
config_name = input()
configfile = open(config_name, "r")

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no "\n"
print(configlist)
print(f'n_lines read: {len(configlist)}')

## Always close your file
configfile.close()
