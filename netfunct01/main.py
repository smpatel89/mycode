#!/usr/bin/env python3
import subprocess

# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + coffeetime)
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds)
            # we'll learn to write code that sends cmds to device here
        print(f'\n')

def devicereboot(ips):
    for ip in ips:
        print(f'Connecting to.. {ip}')
    print(f'REBOOTING NOW')

def get_work():
    # Get ARP cache from /ip neigh/ command sent to shell
    sh_result = subprocess.run(['ip', 'neigh'], stdout=subprocess.PIPE)
    # Parse shell output as UTF-8
    arp_lines = sh_result.stdout.decode('UTF-8').split('\n')

    # Initialize the return dictionary
    ret = {}
    for ip in arp_lines:
        if ip == '': break
        data = ip.split(' ')

        # Dictionary: key = IP, value = array[interface, status]
        ret[data[0]] = [data[2], data[-1]]
    return ret

# start our main script
def main():
    work2do = get_work()

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n" + '\n') # replace with function call that reads in data from file

    ## run
    commandpush(work2do) # call function to push commands to devices
    devicereboot(list(work2do.keys()))

# call our main function
main()
