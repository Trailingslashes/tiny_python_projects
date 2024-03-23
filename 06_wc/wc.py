#!/usr/bin/env python3
"""
Author : <Cole Phillips>
Date   : 2024-03-23
Purpose: word count
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin],
                        help="Input file(s)")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Word Count"""

    args = get_args()

    total_lines = 0
    total_words = 0
    total_char_count = 0

    for file in args.file:
        line_numbers = 0
        char_count = 0
        word_count = 0
        filename = os.path.basename(file.name)

        for line in file:
            line_numbers += 1
            char_count += len(line)
            word_count += len(line.split())

        total_lines += line_numbers
        total_words += word_count
        total_char_count += char_count

        print(f'{line_numbers:8}{word_count:8}{char_count:8} {filename}')

    if len(args.file) > 1:
        print(f'{total_lines:8}{total_words:8}{total_char_count:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
