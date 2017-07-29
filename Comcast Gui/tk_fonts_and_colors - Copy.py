#!/usr/bin/python

import Tkinter as tk

def main():
    app = FontColorDemo()
    app.mainloop()


class FontColorDemo(tk.Tk):
    BIGCODE = ( "Courier",48,"bold" )
    
    def __init__(self):
        tk.Tk.__init__(self)

        label_one = tk.Label(text="This is label ONE",font=FontColorDemo.BIGCODE)
        label_one.pack()


        label_two = tk.Label(
            text="This is the SECOND label",
            foreground="yellow",
            background="darkblue",
            activeforeground="#0CAA59",
            activebackground="darkblue",
        )
        label_two.pack()

        label_three = tk.Label(text="This is label three",font=FontColorDemo.BIGCODE)
        label_three.pack()
        
        label_three.configure(font="-*-Helvetica-Bold-R-Normal--*-180-*-*-*-*-*-*")

        mybutton = tk.Button(text="Push Me",command=self.destroy)
        mybutton.configure( font=("Times", 36, "italic"))
        mybutton.pack()

if __name__ == '__main__':
    main()

