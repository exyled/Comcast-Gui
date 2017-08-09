#!/usr/bin/env python

import Tkinter as tk

def main():
    app = TweakingDemo()
    app.mainloop()
    
class TweakingDemo(tk.Tk):
    PADDING = ( (0,0), (0,5), (5, 5), (5, 10), (10,10) )
    def __init__(self):
        tk.Tk.__init__(self)
        
        frame_left = tk.Frame()
        frame_left.pack(side=tk.LEFT)
    
        for x,y in TweakingDemo.PADDING:
            b = tk.Button(frame_left, text='padx={0} pady={1}'.format(x,y), background='pink')
            b.pack(side=tk.TOP, padx=x, pady=y)

        frame_right = tk.Frame()
        frame_right.pack(side=tk.LEFT)

        for x,y in TweakingDemo.PADDING:
            b = tk.Button(frame_right, text='ipadx={0} ipady={1}'.format(x,y), background='papayawhip')
            b.pack(side=tk.TOP, ipadx=x, ipady=y)

if __name__ == '__main__':
    main()    