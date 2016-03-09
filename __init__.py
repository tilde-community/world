from __future__ import print_function

import sys
import time


# The printer function that should be used all through out the game.
def printer(text):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        time.sleep(0.02)
    print

printer('Welcome to the World!')


# a function that is used when entering the world.
def enter(username):
    pass


# find a monster to fight with.
def find_monster():
    pass


# evaluate the answer given the current monster being fought
def attack(answer):
    pass
