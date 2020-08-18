#!/usr/bin/env python3
"""
Author : chuckconway <charles@cconway.com>
Date   : 2020-08-18
Purpose: Kicking it at home
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        help='Pass any word',
                        metavar='str',
                        type=str, )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = discover_article(word)

    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


def discover_article(word):
    """Discovers if the word is proceeded by an 'a' or an 'an' """

    return 'an' if word[0].lower() in 'aeiou' else 'a'

    # My first attempt
    # vowels = ['a', 'e', 'i', 'o', 'u']
    # first_letter = word[0].lower()
    # article = 'a'
    #
    # for vowel in vowels:
    #     if first_letter == vowel:
    #         article = 'an'
    #
    # return article


# --------------------------------------------------
if __name__ == '__main__':
    main()
