#!/usr/bin/env python3
"""
Author : ame <Cole Phillips>
Date   : 2024-04-04
Purpose: Bottles of Beer
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        metavar='number',
                        type=int,
                        default=10,
                        help='How many bottles')

    args = parser.parse_args()

    if args.num <= 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args

# --------------------------------------------------


def verse(bottle):
    """Sing a verse"""
    next_bottle = bottle - 1
    verse1 = f"{bottle} bottle{'s' if bottle > 1 else ''} of beer on the wall,"
    verse2 = f"{bottle} bottle{'s' if bottle > 1 else ''} of beer,"
    verse3 = "Take one down, pass it around,"
    verse4 = f"{next_bottle if next_bottle != 0 else 'No more'} bottle{'s' if next_bottle != 1 else ''} of beer on the wall!"
    return '\n'.join([verse1, verse2, verse3, verse4])


def main():
    """Make a jazz noise here"""

    args = get_args()

    for i in range(args.num, 0, -1):
        if i != 1:
            print(verse(i))
            print()
        else:
            print(verse(i))


# --------------------------------------------------
if __name__ == '__main__':
    main()
