from __future__ import print_function

import sys
import time

import requests

import settings
import pickle


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


# set up domain
def reset_base_url(reset=False):
    server_domain_url = None
    try:
        with open(r'settings.pkl', 'rb') as f:
            server_domain_url = pickle.load(f)
            settings.domain_url = server_domain_url
            settings.register_url = server_domain_url + 'register/'
            settings.deactivate_url = server_domain_url + 'deactivate/'
            settings.activities_url = server_domain_url + 'activities/'
    except IOError:
        pass
    if reset or server_domain_url is None:
        template = "What is your server domain url?\n" +\
            "(e.g. http://localhost:8888/)\n"
        server_domain_url = raw_input(template)
        settings.domain_url = server_domain_url
        settings.register_url = server_domain_url + 'register/'
        settings.deactivate_url = server_domain_url + 'deactivate/'
        settings.activities_url = server_domain_url + 'activities/'
        with open(r'settings.pkl', 'wb') as f:
            pickle.dump(settings.domain_url, f)
