#!/usr/bin/env python3

ipchk = input('Apply an IP address: ')
if ipchk == '192.168.70.1':
    print(f'Looks like the IP of the gateway was set to {ipchk}. This is not recommended')
elif ipchk:
    print(f'Looks like the IP was set: {ipchk}')
else:
    print('You did not provide input...')
    
