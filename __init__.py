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
        time.sleep(0.01)
    raw_input()


from player import Player
from monsters import create_the_monsters


__monsters = create_the_monsters()
__current_monster = None


# find a monster to fight with.
def find_monster():
    global __current_monster
    global game_data
    if 'player' not in game_data:
        printer('You are not a registered player!')
        printer('User world.enter() to enter the World.')
        return
    elif game_data['player'].level > len(__monsters):
        printer('There are no monsters left in the world!')
        printer('Congratulations {}! You have finished the game.'.format(
            game_data['player'].name))
        return

    game_data['player'].life = level + 5
    i = game_data['player'].level - 1
    monster = __monsters[i]
    __current_monster = monster
    __current_monster.introduction()
    game_data['player'].display_stats()


# evaluate the answer given the current monster being fought
def attack(answer):
    global __current_monster
    global game_data
    if not __current_monster:
        printer('You are not fighting any monster as of now.')
        printer('Use world.find_monster() to fight one.')
        return

    printer('You attacked {0} with your answer.'.format(
        __current_monster.name))

    result = __current_monster.evaluate(answer)
    if result:
        printer('Your answer is correct!')
        game_data['player'].level_up()
        save_game_data()
        __current_monster.defeat()
        __current_monster = None
    else:
        printer('Your answer is wrong!')
        __current_monster.attack()
        game_data['player'].life -= __current_monster.level
        game_data['player'].display_stats()
        if game_data['player'].life <= 0:
            __current_monster = None
            printer('You fainted because of your incompetence.')
            printer('What a loser.')
            printer('Unless you try again...')


# register player to server
def register(player):
    if player.registered:
        return True
    global game_data
    printer('Registering to server...')
    try:
        r = requests.post('http://localhost:8888/register/',
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
    r = requests.post('http://localhost:8888/deactivate/',
                      data={'username': player.name})
    if r.status_code == 200:
        return True
    return False


# get existing player or create a new player
def enter():
    global game_data
    try:
        # load existing
        with open(r'gamedat.pkl', 'rb') as f:
            game_data = pickle.load(f)
        game_data['player']
    except (IOError, KeyError):
        # create new
        printer('Alas, for the intro. What is your name again?')
        name = str(raw_input())
        player = Player(name=name)
        game_data['player'] = player  # save player instance
        save_game_data()
    return game_data['player']


# reset game_data, and unregister player to server
# much like an apocalypse but the host survives, (this time the world)
def reset_world():
    message = 'Are you sure you want to leave this world? (y/n) '
    if (raw_input(message).lower() == 'y'):
        global game_data
        game_data = {}  # this is so creepy! :-o
        save_game_data()  # reset game data
        printer('okay :(')
    else:
        printer("That's the spirit!")


# print help
def ask_help():
    printer('Our hero, here are the functions you can call from this World.')
    printer('world.find_monster()   -> Find a monster to fight.')
    printer('world.attack(answer)   -> Attack the monster with your answer.')
    printer('world.ask_help(answer) -> Print this help section.')
    printer('world.enter()          -> Enter the world.')
    printer('world.reset_world()    -> Reset everything.')


# save game data
def save_game_data():
    global game_data
    with open(r'gamedat.pkl', 'wb') as f:  # reset game_data
        pickle.dump(game_data, f)


# run this function upon import just to keep things tidy
def main():
    printer('Greetings young adventurer!\nWelcome to... The World!')
    player = enter()
    if not player.registered:
        register(player)
    printer('{}! Our chosen one. We are well pleased.'.format(player.name))
    ask_help()

main()
