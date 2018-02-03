from win_explorer_action import *
from path_resolver import *

# \HKEY_CURRENT_USER\Software\Classes\*\shell\Hasher\command
define_action_on(
    '*',
    'Hasher',
    '"{}" "{}" "%1"'.format(get_interpreter_path(), get_main_script_path())
)
