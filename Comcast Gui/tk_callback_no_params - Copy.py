#!/usr/bin/env python

import Tkinter as tk

def main():
    app = CallbackDemo()
    app.mainloop()

class CallbackDemo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self._b1 = tk.Button (
            text="Push Me",
            command=self._make_button_text_red
        )    
        self._b1.pack()

    # callback
    def _make_button_text_red(self):
       self._b1.configure(
           activebackground='red',
           background='red',
       )

if __name__ == '__main__':
    main()