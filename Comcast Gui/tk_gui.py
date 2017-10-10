#!/usr/bin/python
'''Create and configure widgets with Tkinter'''
import Tkinter as tk



def main():
    '''Program entry point -- builds and runs GUI'''
    app = WidgetDemo()
    app.mainloop()

class WidgetDemo(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title("Menu GUI")
        
        lab_hello = tk.Label(text="Hello, this is the GUI for menu items.") 
        lab_hello.configure(foreground="white", background='blue')
        lab_hello.pack()
        
        b_exit = tk.Button(text="Quit", command=self.destroy)
        b_exit.pack()
    

main()