#!/usr/bin/python
'''Add scrollbars to a Text widget'''

import Tkinter as tk
from functools import partial

def main():
    '''Program entry point'''
    app = ScrollBarsDemo()
    app.mainloop()
    

class ScrollBarsDemo(tk.Tk):
    '''Demonstrate adding scroll bars to a Text widget'''
    
    ANIMALS =('lion', 'bear', 'giraffe', 'lemur', 'orangutan', 'elk', 'snail darter',
          'vole', 'african swallow')
    
    COLORS = ('red', 'yellow', 'green', 'blue', 'purple', 'grey', 'pink', 'brown',
            'lavender', 'mauve', 'brown', 'white', 'black', 'navy', 'salmon', 'scarlet')

    def __init__(self):
        tk.Tk.__init__(self)

        self._build_gui()
        self._fill_text(ScrollBarsDemo.ANIMALS)
        
    def _build_gui(self):
        '''Build the GUI'''
    
        self.title("Fun with Text Display")
        
        self._fr_disparea = tk.Frame()
        self._fr_disparea.pack()
        
        self._display_area = tk.Text(self._fr_disparea, height=8, width=50) # size in chars
        self._display_area.pack(side=tk.LEFT)
        
        scroll = tk.Scrollbar(self._fr_disparea)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        
        self._display_area.configure(yscrollcommand = scroll.set)
        scroll.configure(command=self._display_area.yview)
        
        b_animals = tk.Button(text="Fill with animals", command=partial(self._fill_text, ScrollBarsDemo.ANIMALS))
        b_animals.pack()
        
        b_colors = tk.Button(text="Fill with colors", command=partial(self._fill_text, ScrollBarsDemo.COLORS))
        b_colors.pack()
        
        b_quit = tk.Button(text="Quit", command=self.destroy)
        b_quit.pack()
                
        
    
    def _clear_disp(self):
        '''Clear the display'''
        self._display_area.delete('1.0', 'end')    # clear entire window
    
    def _fill_text(self, items):
        '''Fill the display with the list of animals'''
        self._clear_disp()
        for item in items: 
            self._display_area.insert('end', item + "\n")
        

main()