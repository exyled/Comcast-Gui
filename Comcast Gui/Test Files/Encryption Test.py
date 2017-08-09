#!python2
#!/usr/bin/env python

# quicksafe - The easiest way to securely encrypt notes
#
# Copyright (c) 2014 Philipp Emanuel Weidmann <pew@worldwidemann.com>
#
# Nemo vir est qui mundum non reddat meliorem.
#
# Released under the terms of the MIT License
# (http://opensource.org/licenses/MIT)

try:
    # Python 3 imports
    from tkinter import Tk, WORD, BOTH, END
    from tkinter.scrolledtext import ScrolledText
    from tkinter.simpledialog import askstring
    from tkinter.messagebox import showwarning, showerror
except ImportError:
    # Python 2 imports
    from Tkinter import Tk, WORD, BOTH, END
    from ScrolledText import ScrolledText
    from tkSimpleDialog import askstring
    from tkMessageBox import showwarning, showerror
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher.AES import new as AES_new, MODE_CFB, block_size
from Crypto import Random
from zlib import compress, decompress
from base64 import b64encode, b64decode
from tempfile import NamedTemporaryFile
from shutil import copyfile
import sys, textwrap, os, re


# Cryptography methods adapted from http://stackoverflow.com/a/12525165
def get_cipher(password, iv):
    # Key derivation; adjust number of iterations as needed.
    # Note how the initialization vector doubles as a salt
    key = PBKDF2(password, iv, 32, 10000)
    return AES_new(key, MODE_CFB, iv)

def encrypt(data, password):
    # Compress before encrypting
    data = compress(data.encode('utf-8'), 9)
    iv = Random.new().read(block_size)
    return b64encode(iv +
                     get_cipher(password, iv).encrypt(data)).decode('utf-8')

def decrypt(data, password):
    data = b64decode(data)
    iv = data[:block_size]
    return decompress(get_cipher(password, iv).decrypt(data[block_size:]))


def ask_password(caption):
    return askstring(caption, '', show='*').encode('utf-8')

def open_handler():
    global password
    password = ask_password('Enter Password')
    if not password: sys.exit()
    try:
        scrolled_text.insert(END, decrypt(ciphertext, password).decode('utf-8'))
    except Exception:
        # (Most likely) wrong password => try again
        open_handler()

def close_handler():
    global password
    # Omit additional newline returned by ScrolledText widget
    text = scrolled_text.get('1.0', 'end-1c')
    if not password and not text: sys.exit()
    if not password:
        password1 = ask_password('Set Password')
        if not password1: return
        password2 = ask_password('Confirm Password')
        if not password2: return
        if password1 != password2:
            showwarning('Warning', 'Passwords do not match')
            # Try again
            close_handler()
            return
        password = password1
    # To prevent data loss in case something goes wrong while encrypting,
    # first write to a temporary file, then replace this file with it
    try:
        with NamedTemporaryFile(delete=False) as file:
            file.write((match.group(1) + '\n' +
                        textwrap.fill(encrypt(text, password), 80) +
                        '\n' + match.group(3)).encode('utf-8'))
        copyfile(file.name, __file__)
    except Exception as error:
        showerror('Error', 'Unable to save: %s' % str(error))
        return
    finally:
        os.remove(file.name)
    root.destroy()


# Set up GUI
root = Tk(className=' '+os.path.basename(__file__))
root.protocol('WM_DELETE_WINDOW', close_handler)
root.withdraw()
scrolled_text = ScrolledText(root, wrap=WORD, highlightthickness=0)
scrolled_text.pack(fill=BOTH, expand=True)

password = None

# Parse script file
pattern = re.compile(r"(.*^'''\[DATA\])(.*)(\[/DATA\]'''.*)",
                     re.MULTILINE | re.DOTALL)
with open(__file__, 'r') as file:
    match = pattern.match(file.read())

ciphertext = match.group(2).strip()
if ciphertext: open_handler()

root.deiconify()
root.mainloop()


# Encrypted text follows
#
# !!!CAUTION!!!: Do not modify anything after this comment or
#                your text might be permanently lost!

'''[DATA]
[/DATA]'''