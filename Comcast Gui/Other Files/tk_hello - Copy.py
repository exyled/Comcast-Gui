#!/usr/bin/env python
'''Tkinter Hello, world'''
import Tkinter as tk

def main():
    '''Program entry point'''
    app = Hello()
    app.mainloop()

class Hello(tk.Tk):
    '''Hello world in Tkinter implemented as a class'''
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Hello from Tkinter")
        
        lab_hello = tk.Label(text="Hello, Tkinter World") 
        lab_hello.pack()

if __name__ == '__main__':       
    main()