from __future__ import print_function

import sys
import time

import requests


# The printer function that should be used all through out the game.
def printer(text):
    for c in text:
        if c == '\n':
            raw_input()
        print(c, end='')
        sys.stdout.flush()
        time.sleep(0.02)
    raw_input()

printer('Welcome to the World!\nGreetings young adventurer!')


# a function that is used when entering the world.
def enter(username):
    pass


# find a monster to fight with.
def find_monster():
    pass


# evaluate the answer given the current monster being fought
def attack(answer):
    pass


# register player to server
def register(player):
    try:
        r = requests.post('http://localhost:8888/register/',
                          data={'username': player.name})
    except Exception, e:
        printer(e)
        printer('Registration failed. Will try again later.')
        return False
    if 'username' in r.json() and r.json()['username'] == player.name:
        player.registered = True
    return True
