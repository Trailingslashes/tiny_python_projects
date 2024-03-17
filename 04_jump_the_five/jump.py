#!/usr/bin/env python3
"""
Author : Cole Phillips
Date   : 2024-03-16
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Jump the Five"""

    args = get_args()
    str_arg = args.str

    jumper = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5',
    }
    jumped_number = ''
    for char in str_arg:
        jumped_number += jumper.get(char, char)
    print(jumped_number)


# --------------------------------------------------
if __name__ == '__main__':
    main()
