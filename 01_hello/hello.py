#!/usr/bin/env python3
"""
What is the purpose of this script...
"""

import argparse


def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Say Hello')

    parser.add_argument(
        '-n',
        '--name',
        metavar="name",
        default='World',
        help='Name to greet')

    return parser.parse_args()


def main():
    args = get_args()
    print('Hello, ' + args.name + '!')


# Say hello
# print("Hello, World!")

if __name__ == '__main__':
    main()
