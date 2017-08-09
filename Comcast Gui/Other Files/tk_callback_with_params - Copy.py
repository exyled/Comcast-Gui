#!/usr/bin/python

import Tkinter as tk

def main():
    app = CallbackDemo()
    app.mainloop()

class CallbackDemo(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        colors = ('red','green','blue','yellow','purple','pink',
            'papayawhip')
        
        for color in colors:
        
            b = tk.Button(text="Push Me ({0})".format(color))
            b.configure(command=self._make_callback(b,color))
            b.pack()
        
        bye = tk.Button(text="Exit", command=self.destroy)
        bye.pack()
        
    # return a function that will configure the widget
    # (function factory -- AKA closure)
    def _make_callback(self, button, color):
        def turn_color():
            button.configure(activebackground=color)
            button.configure(background=color)
            
        return turn_color  # returns the callback function

if __name__ == '__main__':
    main()