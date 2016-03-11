from __future__ import print_function

import sys
import time

import requests

import settings


# The printer function that should be used all through out the game.
def printer(text):
    for c in text:
        if c == '\n':
            raw_input()
        print(c, end='')
        sys.stdout.flush()
        time.sleep(0.01)
    raw_input()


# api endpoint for activities (GET, POST)
def create_activity(text, kind):
    try:
        r = requests.post(settings.activities_url,
                          data={'text': text, 'kind': kind})
    except:
        return False
    else:
        return r.ok
