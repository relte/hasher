import os, sys

def get_script_dir() -> str:
    return os.path.dirname(os.path.realpath(__file__))

def get_chosen_file_path() -> str:
    return sys.argv[1]

def get_main_script_path() -> str:
    return get_script_dir() + '\main.py'

def get_interpreter_path() -> str:
    return sys.executable.replace('python', 'pythonw')
