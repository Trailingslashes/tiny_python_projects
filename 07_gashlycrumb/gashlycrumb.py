#!/usr/bin/env python3
"""
Author : ame <Cole Phillips>
Date   : 2024-03-23
Purpose: The Gashlycrumb Tinies
"""

import argparse
from pprint import pprint as pp

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Letter(s)',)

    parser.add_argument('-f', '--file',
                        metavar='FILE',
                        default='gashlycrumb.txt',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Gashlycrumb"""

    args = get_args()

    lookup_dict = {}
    for line in args.file:
        lookup_dict[line[0].upper()] = line.rstrip()


    for letter in map(str.upper, args.letter):
        message = lookup_dict.get(letter, f'I do not know "{letter}".')
        pp(message)

# --------------------------------------------------
if __name__ == '__main__':
    main()
