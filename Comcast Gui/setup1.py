import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "guifoo",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Encrypt_txt-Copy.py", base=base)])
		
		
		
		
# -*- coding: utf-8 -*-

# A simple setup script to create an executable using Tkinter. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# SimpleTkApp.py is a very simple type of Tkinter application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

#import sys
#from cx_Freeze import setup, Executable
#
#base = None
#if sys.platform == 'win32':
#    base = 'Win32GUI'
#
#executables = [
#    Executable('SimpleTkApp.py', base=base)
#]
#
#setup(name='simple_Tkinter',
#      version='0.1',
#      description='Sample cx_Freeze Tkinter script',
#      executables=executables
#      )