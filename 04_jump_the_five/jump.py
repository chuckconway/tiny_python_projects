#!/usr/bin/env python3
"""
Author : chuckconway <chuckconway@localhost>
Date   : 2020-08-19
Purpose: Rock the Casbah
"""

import argparse
import re

translate = {
    '1': '9',
    '2': '8',
    '3': '7',
    '4': '6',
    '5': '0',
    '6': '4',
    '7': '3',
    '8': '2',
    '9': '1',
    '0': '5'
}


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('phrase',
                        nargs='+',
                        metavar='items',
                        help='A phrase that contains a phone number.')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    words = args.phrase

    words = codify_phrase(words)
    display = ' '.join(words)

    print(display)


def translate_number(number):
    return translate[number]


def phone_format(n):
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]


def codify_phrase(words):
    count = 0
    new_items = []
    for item in words:
        count = count + 1
        cleaned_number = re.sub(r'\D', '', item)

        if len(cleaned_number) > 6:
            new_values = codify_number(item)
            new_items.append(''.join(new_values))
        else:
            new_items.append(item)

    return new_items


def codify_number(item):
    new_values = []
    for character in item:
        if re.match(r'\d', character):
            coded = translate_number(character)
            new_values.append(coded)
        else:
            new_values.append(character)

    return new_values


# --------------------------------------------------
if __name__ == '__main__':
    main()
