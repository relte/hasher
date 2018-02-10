config = {
    'environment': 'dev',
    'name': 'Hasher'
}

def is_dev_environment():
    return config['environment'] == 'dev'

def get_name():
    return config['name']
