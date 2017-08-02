#!/usr/bin/env python

import Tkinter as tk

def main():
    app = MenubarDemo()
    app.mainloop()

class MenubarDemo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title("Menubar Demo")
        
        menubar = tk.Menu()

        # file menu
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label='Open...', command=self._open_file)
        file_menu.add_command(label='Save', command=self._save_file)
        file_menu.add_command(label='Save as...', command=self._save_file_as)
        file_menu.add_command(label='Quit', command=self.destroy)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # edit menu
        edit_menu = tk.Menu(menubar, tearoff=False)
        edit_menu.add_command(label='Cut', command=self._cut)
        edit_menu.add_command(label='Copy', command=self._copy)
        edit_menu.add_command(label='Paste', command=self._paste)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        
        
        self.config(menu=menubar)
        
        lab1 = tk.Label(text="Menubar DEMO")
        lab1.pack(padx=30, pady=30)
        
    def _open_file(self): pass

    def _save_file(self): pass

    def _save_file_as(self): pass

    def _cut(self): pass

    def _copy(self): pass

    def _paste(self): pass

if __name__ == '__main__':
    main()