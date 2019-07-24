#!/usr/bin/env python3
import sys

print("What is the wind speed (mph)?")
speed = 0
try:
    speed = float(input())
except Exception as e:
    print("Write a number next time...")
    sys.exit(0)

if speed >= 157:
    print("Hurricane CAT5 (Major) -- Hope you have a bomb shelter")
elif speed >= 130:
    print("Hurricane CAT4 (Major) -- Better start runnin'")
elif speed >= 111:
    print("Hurricane CAT3 (Major) -- Better stay indoors")
elif speed >= 96:
    print("Hurricane CAT2 -- Wear a coat")
elif speed >= 74:
    print("Hurricane CAT1 -- Eh. You'll be fine")
else:
    print('Uh. There\'s barely a breeze')

