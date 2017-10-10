# !/usr/bin/env python
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


    ######################
tk_widgets.py
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



####################
tk_button.py
import Tkinter as tk

def main():
    app = ButtonExample()
     app.mainloop()

class ButtonExample(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.button1 = tk.Button (text="Push Me",command=self._doit)
        self.button1.pack()

    def _doit(self):
        self.button1.configure(text="Ouch!")

if __name__ == '__main__':
    main()


###################################
tk_selectable.py
import Tkinter as tk

def main():
    app = SelectableDemo()
    app.mainloop()

class SelectableDemo(tk.Tk):
    def __init__(self):
         tk.Tk.__init__(self)
         self._add_cocoa = tk.StringVar()
         self._add_sugar = tk.StringVar()
         self._add_nutmeg = tk.StringVar()

         self._add_cocoa.set(False)
         self._add_sugar.set(False)
         self._add_nutmeg.set(False)

         c1 = tk.Checkbutton(text="Cocoa",variable=self._add_cocoa)
         c2 = tk.Checkbutton(text="Sugar",variable=self._add_sugar)
         c3 = tk.Checkbutton(text="Nutmeg",variable=self._add_nutmeg)

         self._dairy = tk.StringVar()
         self._dairy.set('milk') # default button

         r1 = tk.Radiobutton(text="Whole Milk",
         value='milk',variable=self._dairy)
         r2 = tk.Radiobutton(text="Half-and-Half",
         value='half',variable=self._dairy)
         r3 = tk.Radiobutton(text="Skim Milk",
         value='skim',variable=self._dairy)
         r4 = tk.Radiobutton(text="2% Milk",
         value='twop',variable=self._dairy)

         for w in (c1,c2,c3,r1,r2,r3,r4):
            w.pack(anchor='w')

        b_quit = tk.Button(text="Quit",command=self.destroy)
        b_quit.pack()

if __name__ == '__main__':
   main()

###########################

tk_text_entry.py
import Tkinter as tk

def main():
    app = TextEntryDemo()
    app.mainloop()

class TextEntryDemo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

         # initialize the main window
         self.title("Text Entry")

         self._entered_text = tk.StringVar()

         self._lab_name = tk.Label(text="Enter name:")
         self._lab_name.pack(anchor='w')

         self._entry_name = tk.Entry(width=25,
textvariable=self._entered_text)
        self._entry_name.pack()

if __name__ == '__main__':
   main()

################################

tk_text_multiline.py
import Tkinter as tk
from functools import partial

def main():
     '''Program entry point'''
     app = TextDemo()
     app.mainloop()

class TextDemo(tk.Tk):
    '''Demonstrate using a Text widget'''

    ANIMALS =('lion', 'bear', 'giraffe', 'lemur', 'orangutan', 'elk', 'snail darter',
        'vole', 'african swallow')

    COLORS = ('red', 'yellow', 'green', 'blue', 'purple', 'grey', 'pink', 'brown',
        'lavender', 'mauve', 'brown', 'white', 'black', 'navy', 'salmon', 'scarlet')
    def __init__(self):
        tk.Tk.__init__(self)

        self._build_gui()
        self._fill_text(TextDemo.ANIMALS)

    def _build_gui(self):
        '''Build the GUI'''

        self.title("Fun with Text Display")


        self._display_area = tk.Text(height=8, width=50) # size in chars
        self._display_area.pack()

        b_animals = tk.Button(
        text="Fill with animals",
        command=partial(self._fill_text, TextDemo.ANIMALS)
        )
        b_animals.pack()

        b_colors = tk.Button(
        text="Fill with colors",
        command=partial(self._fill_text, TextDemo.COLORS)
        )
        b_colors.pack()

        b_quit = tk.Button(text="Quit", command=self.destroy)
        b_quit.pack()



    def _clear_disp(self):
        '''Clear the display'''
        self._display_area.delete('1.0', 'end') # clear entire window

    def _fill_text(self, items):
        '''Fill the display with the list of animals'''
        self._clear_disp()
        for item in items:
            self._display_area.insert('end', item + "\n")

if __name__ == '__main__':
    main()

#########################

tk_listbox.py
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

####################################

# !/usr/bin/python

import tkinter as tk


def main():
    app = SelectableDemo()
    app.mainloop()


class SelectableDemo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._add_passwords = tk.StringVar()
        self._add_phones = tk.StringVar()
        self._add_websites = tk.StringVar()

        self._add_passwords.set(False)
        self._add_phones.set(False)
        self._add_websites.set(False)

        c1 = tk.Checkbutton(text="Passwords", variable=self._add_passwords)
        c2 = tk.Checkbutton(text="Phones", variable=self._add_phones)
        c3 = tk.Checkbutton(text="Websites", variable=self._add_websites)

        self._dairy = tk.StringVar()
        self._dairy.set('milk')  # default button

        r1 = tk.Radiobutton(text="Whole Milk",
                            value='milk', variable=self._dairy)
        r2 = tk.Radiobutton(text="Half-and-Half",
                            value='half', variable=self._dairy)
        r3 = tk.Radiobutton(text="Skim Milk",
                            value='skim', variable=self._dairy)
        r4 = tk.Radiobutton(text="2% Milk",
                            value='twop', variable=self._dairy)

        for w in (c1, c2, c3, r1, r2, r3, r4):
            w.pack(anchor='w')

        b_quit = tk.Button(text="Quit", command=self.destroy)
        b_quit.pack()


if __name__ == '__main__':
    main()

########################################

tk_text_entry.py
# !/usr/bin/env python

import Tkinter as tk


def main():
    app = TextEntryDemo()
    app.mainloop()


class TextEntryDemo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # initialize the main window
        self.title("Text Entry")

        self._entered_text = tk.StringVar()

        self._lab_name = tk.Label(text="Enter name:")
        self._lab_name.pack(anchor='w')

        self._entry_name = tk.Entry(width=25, textvariable=self._entered_text)
        self._entry_name.pack()


if __name__ == '__main__':
    main()

################################

tk_text_multiline.py
# !/usr/bin/python

import Tkinter as tk
from functools import partial


def main():
    '''Program entry point'''
    app = TextDemo()
    app.mainloop()


class TextDemo(tk.Tk):
    '''Demonstrate using a Text widget'''

    ANIMALS = ('lion', 'bear', 'giraffe', 'lemur', 'orangutan', 'elk', 'snail darter',
               'vole', 'african swallow')

    COLORS = ('red', 'yellow', 'green', 'blue', 'purple', 'grey', 'pink', 'brown',
              'lavender', 'mauve', 'brown', 'white', 'black', 'navy', 'salmon', 'scarlet')

    def __init__(self):
        tk.Tk.__init__(self)

        self._build_gui()
        self._fill_text(TextDemo.ANIMALS)

    def _build_gui(self):
        '''Build the GUI'''

        self.title("Fun with Text Display")

        self._display_area = tk.Text(height=8, width=50)  # size in chars
        self._display_area.pack()

        b_animals = tk.Button(
            text="Fill with animals",
            command=partial(self._fill_text, TextDemo.ANIMALS)
        )
        b_animals.pack()

        b_colors = tk.Button(
            text="Fill with colors",
            command=partial(self._fill_text, TextDemo.COLORS)
        )
        b_colors.pack()

        b_quit = tk.Button(text="Quit", command=self.destroy)
        b_quit.pack()

    def _clear_disp(self):
        '''Clear the display'''
        self._display_area.delete('1.0', 'end')  # clear entire window

    def _fill_text(self, items):
        '''Fill the display with the list of animals'''
        self._clear_disp()
        for item in items:
            self._display_area.insert('end', item + "\n")


if __name__ == '__main__':
    main()

##################################

tk_listbox.py
# !/usr/bin/python
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

#########################################

tk_frames.py
# !/usr/bin/python
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

#################################

tk_scrollbars.py
# !/usr/bin/python
'''Add scrollbars to a Text widget'''

import Tkinter as tk
from functools import partial


def main():
    '''Program entry point'''
    app = ScrollBarsDemo()
    app.mainloop()


class ScrollBarsDemo(tk.Tk):
    '''Demonstrate adding scroll bars to a Text widget'''

    ANIMALS = ('lion', 'bear', 'giraffe', 'lemur', 'orangutan', 'elk', 'snail darter',
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

        self._display_area = tk.Text(self._fr_disparea, height=8, width=50)  # size in chars
        self._display_area.pack(side=tk.LEFT)

        scroll = tk.Scrollbar(self._fr_disparea)
        scroll.pack(side=tk.LEFT, fill=tk.Y)

        self._display_area.configure(yscrollcommand=scroll.set)
        scroll.configure(command=self._display_area.yview)

        b_animals = tk.Button(text="Fill with animals", command=partial(self._fill_text, ScrollBarsDemo.ANIMALS))
        b_animals.pack()

        b_colors = tk.Button(text="Fill with colors", command=partial(self._fill_text, ScrollBarsDemo.COLORS))
        b_colors.pack()

        b_quit = tk.Button(text="Quit", command=self.destroy)
        b_quit.pack()

    def _clear_disp(self):
        '''Clear the display'''
        self._display_area.delete('1.0', 'end')  # clear entire window

    def _fill_text(self, items):
        '''Fill the display with the list of animals'''
        self._clear_disp()
        for item in items:
            self._display_area.insert('end', item + "\n")


main()

#############################################

tk_callback_with_params.py
# !/usr/bin/python

import Tkinter as tk


def main():
    app = CallbackDemo()
    app.mainloop()


class CallbackDemo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        colors = ('red', 'green', 'blue', 'yellow', 'purple', 'pink',
                  'papayawhip')

        for color in colors:
            b = tk.Button(text="Push Me ({0})".format(color))
            b.configure(command=self._make_callback(b, color))
            b.pack()

        bye = tk.Button(text="Exit", command=self.destroy)
        bye.pack()

    # return a function that will configure the widget
    # (function factory -- AKA closure)
    def _make_callback(self, button, color):
        def turn_color():
            button.configure(activebackground=color)
            button.configure(background=color)

        return turn_color  # returns the callback function


if __name__ == '__main__':
    main()

###################################

tk_menubar.py
# !/usr/bin/env python

import Tkinter as tk


def main():
    app = MenubarDemo()
    app.mainloop()


class MenubarDemo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Menubar Demo")

        menubar = tk.Menu()

        # file menu
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label='Open...', command=self._open_file)
        file_menu.add_command(label='Save', command=self._save_file)
        file_menu.add_command(label='Save as...', command=self._save_file_as)
        file_menu.add_command(label='Quit', command=self.destroy)
        menubar.add_cascade(label="File", menu=file_menu)

        # edit menu
        edit_menu = tk.Menu(menubar, tearoff=False)
        edit_menu.add_command(label='Cut', command=self._cut)
        edit_menu.add_command(label='Copy', command=self._copy)
        edit_menu.add_command(label='Paste', command=self._paste)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        self.config(menu=menubar)

        lab1 = tk.Label(text="Menubar DEMO")
        lab1.pack(padx=30, pady=30)

    def _open_file(self): pass

    def _save_file(self): pass

    def _save_file_as(self): pass

    def _cut(self): pass

    def _copy(self): pass

    def _paste(self): pass


if __name__ == '__main__':
    main()

####################################





