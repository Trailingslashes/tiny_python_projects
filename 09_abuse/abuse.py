#!/usr/bin/env python3
"""
Author : ame <Cole Phillips>
Date   : 2024-03-30
Purpose: Dial A Curse
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Heap abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        metavar='adjectives',
                        default=2,
                        type=int,
                        help='adjectives')

    parser.add_argument('-n',
                        '--number',
                        metavar='insults',
                        type=int,
                        help='Number of insults',
                        default=3)

    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        type=int,
                        help='Random seed',
                        default=None)

    args = parser.parse_args()

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    adjectives = ['bankrupt', 'base', 'caterwauling', 'corrupt', 'cullionly', 'detestable', 'dishonest', 'false', 'filthsome', 'filthy', 'foolish', 'foul', 'gross', 'heedless', 'indistinguishable', 'infected', 'insatiate', 'irksome', 'lascivious', 'lecherous', 'loathsome', 'lubbery', 'old', 'peevish', 'rascaly', 'rotten', 'ruinous', 'scurilous', 'scurvy', 'slanderous', 'sodden-witted', 'thin-faced', 'toad-spotted', 'unmannered', 'vile', 'wall-eyed']

    nouns = ['Judas', 'Satan', 'ape', 'ass', 'barbermonger', 'beggar', 'block', 'boy', 'braggart', 'butt', 'carbuncle', 'coward', 'coxcomb', 'cur', 'dandy', 'degenerate', 'fiend', 'fishmonger', 'fool', 'gull', 'harpy', 'jack', 'jolthead', 'knave', 'liar', 'lunatic', 'maw', 'milksop', 'minion', 'ratcatcher', 'recreant', 'rogue', 'scold', 'slave', 'swine', 'traitor', 'varlet', 'villain', 'worm']

    for _ in range(args.number):
        print(f"You {', '.join(random.sample(adjectives, k=args.adjectives))} {random.choice(nouns)}!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
