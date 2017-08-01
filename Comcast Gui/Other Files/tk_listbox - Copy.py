#!/usr/bin/python
'''List box example'''

import Tkinter as tk

def main():
    app = ListboxExample()
    app.mainloop()


class ListboxExample(tk.Tk):
    '''Implement a GUI displaying a listbox'''

    LANGUAGES = "Python", "Perl", "PHP", "Ruby", "Awk"

    def __init__(self):
        
        tk.Tk.__init__(self)
        
        self._lab = tk.Label(text="Choose a language")
        self._lab.pack()
        
        self._langlist = tk.Listbox(width=20, height=3)
        self._langlist.insert('end', *ListboxExample.LANGUAGES)
        self._langlist.pack()
                
        b_choose = tk.Button(text="Choose", command=self._update_label)
        b_choose.pack()
        
        b_quit = tk.Button(text="Quit", command=self.destroy)
        b_quit.pack()

    def _update_label(self):
        lang = self._langlist.get(self._langlist.curselection()) 
        self._lab.configure(text="#!/usr/bin/" + lang.lower())

if __name__ == '__main__':
    main()
    



