from __future__ import print_function

import sys
import time


# The printer function that should be used all through out the game.
def printer(text):
    for c in text:
        if c == '\n':
            raw_input()
        print(c, end='')
        sys.stdout.flush()
        time.sleep(0.02)
    raw_input()


# a function that is used when entering the world.
def enter(username):
    pass


# find a monster to fight with.
def find_monster():
    pass


# evaluate the answer given the current monster being fought
def attack(answer):
    pass


# run this function upon import just to keep things tidy
def main():
    printer('Welcome to the World!\nGreetings young adventurer!')


main()
