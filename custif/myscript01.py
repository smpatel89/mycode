#!/usr/bin/env python3
message = 'The movie is about to begin, we recomend '
print('What is your connection speed in Mbps?')
connection = float(input())
if connection >= 25:
    message += 'setting video to 4k.'
elif connection >= 5:
    message += 'setting video to 1080p.'
elif connection >= 2:
    message += 'setting video to 720p.'
else:
    message += 'finding another access network.'
print(message)

