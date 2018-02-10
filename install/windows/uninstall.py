import winreg
import config

# \HKEY_CURRENT_USER\Software\Classes\*\shell\Hasher\command

registry_title = config.get_name()

environmentKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Classes\*\shell', 0, winreg.KEY_ALL_ACCESS)
applicationKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Classes\*\shell\%s' % registry_title, 0, winreg.KEY_ALL_ACCESS)

winreg.DeleteKey(applicationKey, 'command')
winreg.DeleteKey(environmentKey, 'Hasher')
