import winreg
import config
import os, sys
import path_resolver

# \HKEY_CURRENT_USER\Software\Classes\*\shell\Hasher\command

registry_title = config.get_name()
if getattr(sys, 'frozen', False):
    command = '"{}" "%1"'.format(os.path.join(path_resolver.get_root_dir(), 'hasher.exe'))
else:
    command = '"{}" "{}" "%1"'.format(path_resolver.get_interpreter_path(), path_resolver.get_main_script_path())

reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Classes', 0, winreg.KEY_SET_VALUE)
fileTypeKey = winreg.CreateKey(reg, '*')
environmentKey = winreg.CreateKey(fileTypeKey, 'shell')
applicationKey = winreg.CreateKey(environmentKey, registry_title)
commandKey = winreg.CreateKey(applicationKey, 'command')

winreg.SetValueEx(commandKey, None, 0, winreg.REG_SZ, command)
winreg.SetValueEx(applicationKey, 'Icon', 0, winreg.REG_SZ, path_resolver.get_icon_path())

winreg.CloseKey(applicationKey)
winreg.CloseKey(environmentKey)
winreg.CloseKey(fileTypeKey)
winreg.CloseKey(reg)
