"""
Here is defined the core of grepy
"""

from sys import argv


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
    try:
        with open(file=argv[2], mode="r", encoding="UTF-8") as file:
            grep(argv[1], file)
    except FileNotFoundError:
        print("That's not a vaild file.")
    except IndexError:
        print("Params missing!")
