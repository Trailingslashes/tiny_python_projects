#!/usr/bin/env python3
"""
Author : colephillips <colephillips@localhost>
Date   : 2024-03-06
Purpose: Say Hello
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Say hello',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--name',
                        metavar='str',
                        default='World',
                        help='Say hello!')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Say hello

    Args:
        name (str): name to say hello to

    Returns:
        None

    """
    args = get_args()
    str_arg = args.name

    print(f"Hello, {str_arg}!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
