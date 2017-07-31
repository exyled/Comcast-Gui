#!/usr/bin/python
import Tkinter as tk

def main():
    app = FrameExample()
    app.mainloop()

class FrameExample(tk.Tk):
    '''Example of using Frames for layout'''
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Frames')

        f_top = tk.Frame()
        f_top.pack()
        f_bottom = tk.Frame()
        f_bottom.pack()

        tb1 = tk.Button(f_top, text="A")
        tb2 = tk.Button(f_top, text="B")
        tb3 = tk.Button(f_top, text="C")
        
        tb1.pack(side="left")
        tb2.pack(side="left")
        tb3.pack(side="left")

        bb1 = tk.Button(f_bottom, text="X")
        bb2 = tk.Button(f_bottom, text="Y")
        bb3 = tk.Button(f_bottom, text="Z")
        
        bb1.pack(side="left")
        bb2.pack(side="left")
        bb3.pack(side="left")

if __name__ == '__main__':
    main()

