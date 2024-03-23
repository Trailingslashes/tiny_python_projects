#!/usr/bin/env python3
"""
Author : <Cole Phillips>
Date   : 2024-03-23
Purpose: Howler (upper-cases input)
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='text',
                        help='Input a string or a file')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='str',
                        help='Output filename (default: )')

    args = parser.parse_args()

    if os.path.isfile(args.positional):
        args.positional = open(args.positional).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Howler (upper-cases input)"""

    args = get_args()

    if not args.positional:
        print("error: the following arguments are required: text")
        sys.exit(1)
    if args.outfile:
        output_file = open(args.outfile, 'wt')
    else:
        output_file = sys.stdout
    output_file.write(args.positional.upper() + '\n')
    output_file.close()

    # elif os.path.isfile(pos_arg):
    #     with open(pos_arg, 'r') as fh:
    #         contents = fh.read()
    #         print(contents.upper())
    # elif pos_arg:
    #     print(f"{pos_arg.upper()}")
    # elif output_arg:
    #     with open(contents) as fh:
    #         fh.write(pos_arg.upper())

    # try:
    #     if pos_arg and os.path.isfile(pos_arg):

    #     else:
    #         raise FileNotFoundError("File does not exist!")
    # except FileNotFoundError as e:
    #     print(e)


# --------------------------------------------------
if __name__ == '__main__':
    main()
