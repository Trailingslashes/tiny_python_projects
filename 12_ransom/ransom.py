#!/usr/bin/env python3
"""
Author : ame <Cole Phillips>
Date   : 2024-04-10
Purpose: Ransom letter
"""

import argparse
import os
import random

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file',
                        type=str)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

# Functions
# --------------------------------------------------


def choose(char):
    """Randomly choose an upper or lowercase letter to return"""
    return char.upper() if random.choice([0, 1]) else char.lower()

# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    ransom = ""
    for char in args.text:
        ransom += " ".join(choose(char))
    print(ransom)


# --------------------------------------------------
if __name__ == '__main__':
    main()
