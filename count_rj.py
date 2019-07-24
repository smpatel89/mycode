#!/usr/bin/env python3 
r_counter = 0
r_mentioned_counter = 0
j_counter = 0
j_mentioned_counter = 0

with open('romeo.txt') as rj_file:
    for line in rj_file:
        if line.strip() == 'ROMEO':
            r_counter += 1
        else:
            if 'romeo' in line.lower():
                r_mentioned_counter += 1
        if line.strip() == 'JULIET':
            j_counter += 1
        else:
            if 'juliet' in line.lower():
                j_mentioned_counter += 1

print(f'Romeo spoke {r_counter} times')
print(f'Romeo mentioned  by someone else {r_mentioned_counter} times')
print(f'Juliet spoke {j_counter} times')
print(f'Juliet mentioned  by someone else {j_mentioned_counter} times')
