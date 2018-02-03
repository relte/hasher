import winreg

# http://sbirch.net/tidbits/context_menu.html
def define_action_on(filetype: str, registry_title: str, command: str, title=None) -> None:
    """
    filetype: an extension type (ex. ".txt") or one of the special values ("*" or "Directory")
    registry_title: the title of the subkey
    """
    reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Classes", 0, winreg.KEY_SET_VALUE)
    k1 = winreg.CreateKey(reg, filetype) #handily, this won't delete a key if it's already there.
    k2 = winreg.CreateKey(k1, "shell")
    k3 = winreg.CreateKey(k2, registry_title)
    k4 = winreg.CreateKey(k3, "command")
    if title != None:
        winreg.SetValueEx(k3, None, 0, winreg.REG_SZ, title)
    winreg.SetValueEx(k4, None, 0, winreg.REG_SZ, command)
    winreg.CloseKey(k3)
    winreg.CloseKey(k2)
    winreg.CloseKey(k1)
    winreg.CloseKey(reg)
