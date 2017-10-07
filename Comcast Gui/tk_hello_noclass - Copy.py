#!/usr/bin/python
'''Tkinter "Hello, world'''

import Tkinter as tk

def main():
    '''Program entry point'''
    top = build_gui()
    top.mainloop()


def build_gui():
    '''Build the GUI and return the mainwindow object'''
    top = tk.Tk()
    top.title("Hello from Tkinter")

    lab_hello = tk.Label(top, text="Hello, Tkinter World") 
    lab_hello.pack()
    
    return top

main()
