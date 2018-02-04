import os, sys

def get_script_dir() -> str:
    return os.path.dirname(os.path.realpath(__file__))

def get_main_script_path() -> str:
    return os.path.join(get_script_dir(), 'main.py')

def get_icon_path() -> str:
    return os.path.join(get_script_dir(), 'hash.ico')

def get_interpreter_path() -> str:
    return sys.executable.replace('python', 'pythonw')

def get_selected_file_path() -> str:
    return sys.argv[1]

def get_test_file_path() -> str:
    return os.path.join(get_script_dir(), 'tests', 'examples', 'file.txt')
