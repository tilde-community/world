from __future__ import print_function

import pickle
import sys
import time

import requests

"""
Persist game_data via pickle
info include
player    the player instance, should you set/unset you must call
          save_game_data() afterwards
"""
game_data = {}


# The printer function that should be used all through out the game.
def printer(text):
    for c in text:
        if c == '\n':
            raw_input()
        print(c, end='')
        sys.stdout.flush()
        time.sleep(0.02)
    raw_input()


from player import Player
import settings


# a function that is used when entering the world.
def enter():
    printer('Alas, for the intro. What is your name again?')
    name = str(raw_input())
    player = Player(name=name)
    return player


# find a monster to fight with.
def find_monster():
    pass


# evaluate the answer given the current monster being fought
def attack(answer, *args, **kwargs):
    save_game_data()  # pre save game_data
    # insert implementation here
    save_game_data()  # post save game_data


# register player to server
def register(player):
    if player.registered:
        return True
    global game_data
    printer('Registering to server...')
    try:
        r = requests.post(settings.register_url,
                          data={'username': player.name})
    except Exception, e:
        printer(e)
        printer('... failed! :( . Will try again later.')
        return False

    if r.status_code == 403:
        printer('... failed! with code {} :( .\
        Username is already taken.'.format(r.status_code))
        return False
    elif r.status_code != 200:
        printer('... failed! with code {} :( .'.format(r.status_code))
        return False

    if 'username' in r.json() and r.json()['username'] == player.name:
        player.registered = True
        game_data['player'] = player
        save_game_data()  # save game data
        printer('... success for user {} ! :) .'.format(player.name))
    return True


# unregister player to server
def unregister(player):
    r = requests.post(settings.deactivate_url, data={'username': player.name})
    if r.status_code == 200:
        return True
    return False


# get existing player or create a new player
def get_or_create_player():
    global game_data
    try:
        # load existing
        with open(r'gamedat.pkl', 'rb') as f:
            game_data = pickle.load(f)
        game_data['player']
    except (IOError, KeyError):
        # create new
        player = enter()
        game_data['player'] = player  # save player instance
        with open(r'gamedat.pkl', 'wb') as f:
            pickle.dump(game_data, f)
    return game_data['player']


# reset game_data, and unregister player to server
# much like an apocalypse but the host survives, (this time the world)
def reset_world():
    if (raw_input('Are you sure you want to leave this world? (y/n) ').lower()
            == 'y'):
        global game_data
        try:
            unregistered = unregister(game_data['player'])
        except requests.ConnectionError:
            printer("Nope! The almighty won't permit you. :P")
        else:
            if unregistered:
                game_data = {}  # this is so creepy! :-o
                save_game_data()  # reset game data
                printer('okay :(')
            else:
                printer("Nope! The almighty server won't permit you. :P")
    else:
        printer("That's the spirit!")


# save game data
def save_game_data():
    global game_data
    with open(r'gamedat.pkl', 'wb') as f:  # reset game_data
        pickle.dump(game_data, f)


# load game data
def load_game_data():
    global game_data
    with open(r'gamedat.pkl', 'rb') as f:
        game_data = pickle.load(f)


# run this function upon import just to keep things tidy
def main():
    printer('Welcome to the World!\nGreetings young adventurer!')
    player = get_or_create_player()
    if not player.registered:
        register(player)
    printer('{}! Our chosen one. I am well pleased.'.format(player.name))

main()
