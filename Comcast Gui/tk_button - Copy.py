#!/usr/bin/python

import Tkinter as tk

def main():
    app = ButtonExample()
    app.mainloop()

class ButtonExample(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.button1 = tk.Button (text="Push Me",command=self._doit)
        self.button1.pack()

    def _doit(self):
       self.button1.configure(text="Ouch!")

if __name__ == '__main__':
    main()
