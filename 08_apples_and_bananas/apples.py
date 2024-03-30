#!/usr/bin/env python3
"""
Author : ame <Cole Phillips>
Date   : 2024-03-30
Purpose: Apples and Bananas
"""

import argparse
import os
import re

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and Bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='Input text or file',
                        metavar='text',
                        type=lambda t: argparse.FileType('rt')(t) if os.path.isfile(t) else t)

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        choices='aeiou',
                        default='a')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    v_arg = args.vowel
    replaced_text = ''

    flags = re.IGNORECASE
    for char in args.text:
        if char.isupper():
            replaced_text += re.sub('[aeiouAEIOU]', v_arg, char, flags=flags).upper()
        elif char.islower():
            replaced_text += re.sub('[aeiouAEIOU]', v_arg, char, flags=flags).lower()
        else:
            replaced_text += re.sub('[aeiouAEIOU]', v_arg, char, flags=flags)

    print(replaced_text.strip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
