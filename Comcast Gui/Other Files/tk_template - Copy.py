#!/usr/bin/env python

import Tkinter as tk

def main():
    app = AppName()
    app.mainloop()

class AppName(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        # initialize the main window
        self.title("Temporary Title")
        self.geometry("250x50")
        
        # create widgets here...
        # e.g.
        self.b1 = tk.Button (text="Push Me",command=self._doit)
        self.b1.pack()

    # create helper methods and event handlers as needed
    def _doit(self):
       self.b1.configure(text="Ouch!")

if __name__ == '__main__':
    main()