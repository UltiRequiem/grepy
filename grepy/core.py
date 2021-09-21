"""
Here is defined the core of grepy
"""

import argparse


def get_arguments():
    """
    Get Arguments
    """
    parser = argparse.ArgumentParser("Sech for a word in a file.")
    parser.add_argument("file")
    parser.add_argument("string")

    args = parser.parse_args()

    return args.file, args.string


def grep(word, file):
    """
    Sear for the word param in the file param.
    """
    for line in file:
        if word in line:
            print(line.strip())


def main():
    """
    Entry Point of The Program
    """
    string, file = get_arguments()

    try:
        with open(file=file, mode="r", encoding="UTF-8") as file:
            grep(string, file)
    except FileNotFoundError:
        print("That's not a vaild file.")
    except IndexError:
        print("Params missing!")
