import path_resolver
import json
import os

with open(os.path.join(path_resolver.get_script_dir(), 'config.json')) as file:
    config = json.load(file)

def is_dev_environment():
    return config['environment'] == 'dev'

def get_name():
    return config['name']
