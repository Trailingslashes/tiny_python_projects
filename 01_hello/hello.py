#!/usr/bin/env python3
"""
Author : colephillips <colephillips@localhost>
Date   : 2024-03-06
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Say hello',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n','--name',
                        metavar='str',
                        default='World',
                        help='The name to greet')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Say hello"""

    args = get_args()
    # get args
    str_arg = args.name
    
    print(f"Hello, {str_arg}!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
