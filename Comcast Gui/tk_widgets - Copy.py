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
        
        self.title("Hello from Tkinter")
        
        lab_hello = tk.Label(text="Hello, Tkinter World") 
        lab_hello.configure(foreground="white", background='blue')
        lab_hello.pack()
        
        b_exit = tk.Button(text="Quit", command=self.destroy)
        b_exit.pack()
    

main()