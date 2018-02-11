import os, sys


def get_root_dir() -> str:
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.realpath(__file__))


def get_main_script_path() -> str:
    return os.path.join(get_root_dir(), 'main.py')


def get_interpreter_path() -> str:
    return sys.executable.replace('python', 'pythonw')


def get_selected_file_path() -> str:
    return sys.argv[1]


def get_icon_path() -> str:
    return os.path.join(get_data_directory(), 'hasher.ico')


def get_test_file_path() -> str:
    return os.path.join(get_data_directory(), 'example', 'file.txt')


def get_data_directory() -> str:
    return os.path.join(get_root_dir(), 'data')
