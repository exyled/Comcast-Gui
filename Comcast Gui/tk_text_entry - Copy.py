#!/usr/bin/env python

import Tkinter as tk

def main():
    app = TextEntryDemo()
    app.mainloop()

class TextEntryDemo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        # initialize the main window
        self.title("Text Entry")
        
        self._entered_text = tk.StringVar()
        
        self._lab_name = tk.Label(text="Enter name:")
        self._lab_name.pack(anchor='w')
        
        self._entry_name = tk.Entry(width=25, textvariable=self._entered_text)
        self._entry_name.pack()

if __name__ == '__main__':
    main()