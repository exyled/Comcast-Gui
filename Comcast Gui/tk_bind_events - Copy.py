#!/usr/bin/python

import Tkinter as tk

def main():
    '''Program entry point'''
    app = BindExample()
    app.mainloop()
    
class BindExample(tk.Tk):
    '''Demonstrates event binding'''
    def __init__(self):
        tk.Tk.__init__(self)

        self._lab = tk.Label(text="Press Something...")
        self._lab.pack()
        
        b_quit = tk.Button(text="Quit", command=self.destroy)
        b_quit.pack()
        
        self.bind("<a>",self._make_callback("a"))
        self.bind("<Control-a>",self._make_callback("Ctrl-A"))
        self.bind("<Alt-a>",self._make_callback("Alt-A"))
        self.bind("<Shift-A>",self._make_callback("Shift-A"))
        
        self.bind("<Escape>",self._make_callback("Escape key"))
        self.bind("<3>",self._make_callback("right button"))
        
        self.bind("<Unmap>",self._make_callback("window back"))

    def _make_callback(self, text_to_display):
        '''Return a callback for a particular string'''
        def tmp(w):
            self._lab.configure(text=text_to_display)
        return tmp

if __name__ == '__main__':
    main()
