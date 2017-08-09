#!/usr/bin/python

import tkinter as tk

def main():
    app = SelectableDemo()
    app.mainloop()
    
class SelectableDemo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._add_passwords = tk.StringVar()
        self._add_phones = tk.StringVar()
        self._add_websites = tk.StringVar()
        
        self._add_passwords.set(False)
        self._add_phones.set(False)
        self._add_websites.set(False)
        
        c1 = tk.Checkbutton(text="Passwords",variable=self._add_passwords)
        c2 = tk.Checkbutton(text="Phones",variable=self._add_phones)
        c3 = tk.Checkbutton(text="Websites",variable=self._add_websites)

        self._dairy = tk.StringVar()
        self._dairy.set('milk') # default button

        r1 = tk.Radiobutton(text="Whole Milk",
           value='milk',variable=self._dairy)
        r2 = tk.Radiobutton(text="Half-and-Half",
           value='half',variable=self._dairy)
        r3 = tk.Radiobutton(text="Skim Milk",
           value='skim',variable=self._dairy)
        r4 = tk.Radiobutton(text="2% Milk",
           value='twop',variable=self._dairy)

        for w in (c1,c2,c3,r1,r2,r3,r4):
            w.pack(anchor='w')

          
        b_quit = tk.Button(text="Quit",command=self.destroy)
        b_quit.pack()

if __name__ == '__main__':
    main()