#!/usr/bin/env python3
"""Alta3 Research || Author: Me"""

def main():
    """Run-time code"""
    # create a small string
    in_string = "#Header*Bullet1*Bullet2>This is the start of a paragraph"
    print(f'INPUT STRING:\n"{in_string}"\n\n')

    out_string = in_string .replace(">", "\n  ")
    out_string = out_string.replace("*", "\n\t- ")
    out_string = out_string.replace("#", "")

    print(f'OUTPUT STRING:\n{out_string}')

main()

