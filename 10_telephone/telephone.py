#!/usr/bin/env python3
"""
Author : ame <Cole Phillips>
Date   : 2024-04-01
Purpose: Telephone
"""

import argparse
import random
import os
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if args.mutations < 0 or args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    random.seed(args.seed)

    number_of_mutations = round(len(text) * args.mutations)
    alpha = string.ascii_letters + string.punctuation
    sample_index = random.sample(range(len(text)), number_of_mutations)
    new_text = text
    
    # for index, char in enumerate(text):
    #     if index in sample_index:
    #         if char.isalnum():  # Check if the character is alphanumeric
    #             new_text += random.choice(alpha)
    #         else:
    #             new_text += char  # Preserve non-alphanumeric characters
    #     else:
    #         new_text += char
    

    for index in sample_index:
        new_character = random.choice(alpha.replace(text[index], ''))
        new_text = new_text[:index] + new_character + new_text[index + 1:]


    print(f'You said: "{text}"')
    print(f'I heard : "{new_text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
