import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
try:
    # Python 3 imports
    from tkinter import Tk, WORD, BOTH, END
    from tkinter.scrolledtext import ScrolledText
    from tkinter.simpledialog import askstring
    from tkinter.messagebox import showwarning, showerror

#from Crypto.Protocol.KDF import PBKDF2
#from Crypto.Cipher.AES import new as AES_new, MODE_CFB, block_size
#from Crypto import Random
#from zlib import compress, decompress
#from base64 import b64encode, b64decode
#from tempfile import NamedTemporaryFile
#from shutil import copyfile
#import sys, textwrap, os, re

# GUI applications require a different base on Windows (the default is for a
# console application).
#base = None
#base = "Win32GUI"
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name='Comcast Gui',
    version='',
    packages=[''],
    url='',
    license='',
    author='jkern204',
    author_email='',
    description=''
#    executables = [Executable("Encrypt_txt-Copy.py", base=base)])
)