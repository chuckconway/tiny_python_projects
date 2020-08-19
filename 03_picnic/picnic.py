#!/usr/bin/env python3
"""
Author : chuckconway <chuckconway@localhost>
Date   : 2020-08-18
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Our picnic items')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the passed in items.',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    items = args.items
    sort_items = args.sorted
    # Add commas when there are more than one times, also add "and"

    if sort_items:
        items.sort()

    item_output = ''
    items_length = len(items)

    if items_length == 2:
        last_item = items[-1]
        other_items = items[0:items_length - 1]
        item_output = ", ".join(other_items) + ' and ' + last_item

    if items_length > 2:
        last_item = items[-1]
        other_items = items[0:items_length - 1]
        item_output = ", ".join(other_items) + ', and ' + last_item

    if items_length == 1:
        item_output = items[0]

    print(f"You are bringing {item_output}.")


# --------------------------------------------------
if __name__ == '__main__':
    main()
