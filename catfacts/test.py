#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import pprint

def main():
    """Run time code"""
    ## create r, which is our request object
    num = input('Which comic number do you want? ')
    r = requests.get(f'http://xkcd.com/{num}/info.0.json')
    pprint.pprint(r.json())

main()
