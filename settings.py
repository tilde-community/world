
domain_url = 'http://localhost:8888/'
register_url = domain_url + 'register/'
deactivate_url = domain_url + 'deactivate/'
activities_url = domain_url + 'activities/'

# Check to see if there are any overrides in dev_settings
try:
    from local_settings import *
except ImportError:
    pass
