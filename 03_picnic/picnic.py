#!/usr/bin/env python3
"""
Author : ame colephillips
Date   : 2024-03-16
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Picnic game"""

    args = get_args()
    pos_arg = args.items
    flag_arg = args.sorted
    items_indexes = len(pos_arg)
    # sort the list if -s is set
    if flag_arg:
        pos_arg.sort()

    if items_indexes == 1:
        print(f"You are bringing {pos_arg[0]}.")
    elif items_indexes == 2:
        print(f"You are bringing {pos_arg[0]} and {pos_arg[1]}.")
    elif items_indexes == 3:
        print(f"You are bringing {pos_arg[0]}, {pos_arg[1]}, and {pos_arg[2]}.")
    elif items_indexes == 4:
        print(f"You are bringing {pos_arg[0]}, {pos_arg[1]}, {pos_arg[2]}, and {pos_arg[3]}.")
    elif items_indexes >= 5:
        print(f"You are bringing {pos_arg[0]}, {pos_arg[1]}, {pos_arg[2]}, {pos_arg[3]}, and {pos_arg[4]}.")


# --------------------------------------------------
if __name__ == '__main__':
    main()
