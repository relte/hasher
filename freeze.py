import sys, os
from cx_Freeze import setup, Executable

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))

os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base = 'Win32GUI' if sys.platform == 'win32' else None

buildOptions = dict(
    packages=[],
    excludes=[],
    include_files=[
        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
        'data'
    ]
)

executables = [
    Executable('main.py', base=base, targetName='hasher.exe'),
    Executable(os.path.join('setup', 'windows', 'install.py'), base=base, targetName='install.exe'),
    Executable(os.path.join('setup', 'windows', 'uninstall.py'), base=base, targetName='uninstall.exe')
]

setup(name='Hasher',
      version='0.1.0',
      description='A program to generate file hashes from Windows Explorer context menu',
      options=dict(build_exe=buildOptions),
      executables=executables)
