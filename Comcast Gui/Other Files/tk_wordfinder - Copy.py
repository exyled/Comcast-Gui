#!/usr/bin/python

import Tkinter as tk
import tkFileDialog
import re
import os.path

def main():
    app = WordFinder()
    app.mainloop()

class WordFinder(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title("Word Finder")
        self.geometry('400x300')
        
        menubar = tk.Menu()

        # file menu
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label='Load...', command=self._load_file)
        file_menu.add_command(label='Quit', command=self.destroy)
        menubar.add_cascade(label="File", menu=file_menu)
        self.configure(menu=menubar)

        self._file_label = tk.Label(text="")
        self._file_label.pack(anchor=tk.W)
        
        # Add a label for the RE entry blank
        re_label = tk.Label(text="Enter RE:")
        re_label.pack(anchor=tk.W)
        
        
        # Add the RE entry blank
        self._RE_TEXT = tk.StringVar()
        self._re_entry  = tk.Entry(textvariable=self._RE_TEXT)  # needs more work
        self._re_entry.pack(fill=tk.X)

        # Add a checkbox to control whether the search is case sensitive
        self._ignorecase = tk.IntVar()
        ic = tk.Checkbutton(text="Case insensitive", variable=self._ignorecase)
        ic.pack(anchor="w")
        
        # Add a checkbox to control whether the pattern must match the entire word
        self._wc = tk.IntVar()
        self._ww = tk.Checkbutton(text="Match entire word", variable=self._wc)
        self._ww.pack(anchor="w")
        
        # Add a label for the results
        self._results= tk.Label(text="")
        self._results.pack()
        
        listframe=tk.Frame()
        listframe.pack(expand=True, fill=tk.BOTH)
        
        # Add a scroll Text widget with scrollbars
        self._list = tk.Text(listframe, height=5, width=20)
        self._list.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        
        scrollbar =  tk.Scrollbar(listframe)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        
        self._list.configure(yscrollcommand = scrollbar.set)
        scrollbar.configure(command=self._list.yview)
        
        # create a frame to hold the bottom two buttons
        buttonframe = tk.Frame()
        
        # add search & exit buttons to the frame
        self._search = tk.Button(buttonframe, text="Search", command=self._do_search)
        self._exit = tk.Button(buttonframe, text="Exit", command=self.destroy)
        
        # the buttons get packed into buttonframe
        self._search.pack(side="left")
        self._exit.pack(side="left")
        
        # then buttonframe gets backed into the main window
        buttonframe.pack()
        
        # the do_search subroutine is bound to the Enter key, so 
        # pressing Enter has the same effect as pressing the Search button
        self._re_entry.bind("<Return>",self._do_search)
        
        self._file_lines = []

    def _load_file(self):
        file_to_load = tkFileDialog.askopenfile()
        if file_to_load:
            self._file_lines = file_to_load.readlines()
            short_name = os.path.basename(file_to_load.name)
            self._file_label.configure(text="Searching: " + short_name)
            
    # function called when the user presses the Enter key or clicks on the 
    # Search button
    def _do_search(self, event=None):
        count = 0
        matches = 0
    
        self._list.delete('0.0','end')   # clear display window
        
        if self._ignorecase.get():
            opt = "(?i)"
        else:
            opt = "" # is the ignore case button pressed?
                     # any part of RE preceded by (?i)
                     # is matched caseinsensitively
    
        re_text = self._RE_TEXT.get()
        if self._wc.get():
            # entire word must match pattern
            cre = re.compile("^" + opt + re_text + "$")
        else:
            cre = re.compile(opt + re_text)
    
        for line in self._file_lines:
            if cre.search(line):
                #todo: use finditer, m.start() etc to tag matches
                # make matches in red
                self._list.insert('end', line)     # put results in list
                matches += 1                     # count number of matches
            count += 1                        # count total number of words
       # update the label that says how many lines were matched
        self._results.configure(text="{0} lines matched out of {1}".format(matches, count))

if __name__ == '__main__':
    main()
