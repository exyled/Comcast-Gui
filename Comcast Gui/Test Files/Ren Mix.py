#!/usr/bin/python
##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu


##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

##Main Menu Group 1 Buttons
    frame:
        style_group "mm"
        xalign .002
        yalign .00

        has vbox

        textbutton _("1. LDAP Info") action ShowMenu('group1_button1')
        textbutton _("2. Other") action ShowMenu('group1_button2')
        textbutton _("3. Other Menu") action ShowMenu('group1_button3')
        textbutton _("4. KA Servers") action ShowMenu('group1_button4')
#The two buttons below jump to external scripts
        textbutton _("4. Menu1") action ShowMenu('menu_one')
        textbutton _("4. Tips") action [Jump('tips')]
        textbutton _("5. Main Menu 2") action ShowMenu('main_menu_2')
        textbutton _("6. Main Menu 3") action ShowMenu('main_menu_3')
        textbutton _("7. Preferences") action ShowMenu('group1_button9')
        textbutton _("8. Help") action ShowMenu('group1_button10')
        textbutton _("9. Quit") action ShowMenu('group1_button11')
        textbutton _("Unused 1") action ShowMenu('group1_button12')
        textbutton _("Unused 2") action ShowMenu('group1_button13')
        textbutton _("Unused 3") action ShowMenu('group1_button14')
        textbutton _("Unused 4") action ShowMenu('group1_button15')
        textbutton _("Unused 5") action ShowMenu('group1_button16')
        textbutton _("Unused 6") action ShowMenu('group1_button17')
        textbutton _("Unused 7") action ShowMenu('group1_button18')
        textbutton _("Unused 8") action ShowMenu('group1_button19')

##Main Menu Quit Button
    frame:
        style_group "mm"
        xalign .999
        yalign .99

        has vbox

        textbutton _("Quit") action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"

##############################################################################
# group1_button2 menu

screen group1_button2():

    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("LDAP Info") action Start()
        textbutton _("Other") action ShowMenu("other")
        textbutton _("Other Menu") action ShowMenu("other_menu")
        textbutton _("KA Servers") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Help") action Help()
        textbutton _("Return to Previous Menu") action Return()
        textbutton _("Quit") action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"










import tkinter as tk

def main():
    app = menu_one()
    app.mainloop()

class menu_one(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)


===================================================
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
=================================================
##Menubar and one button as well as the selection working together - 7-14-2017
import tkinter as tk

def main():
    app = MenubarDemo()
    app.mainloop()

class MenubarDemo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Comcast DemoBar")

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

        lab1 = tk.Label(text="Comcast DemoBar")
        lab1.pack(padx=30, pady=30)

        self.button1 = tk.Button(text="Push Me Please Daddy!", command=self._doit)
#        self.button2 = tk.Button(text="Holder", command=self._doit)
#        self.button3 = tk.Button(text="Holder", command=self._doit)
#        self.button4 = tk.Button(text="Holder", command=self._doit)
#        self.button4 = tk.Button(text="Holder", command=self._doit)
#        self.button5 = tk.Button(text="Holder", command=self._doit)
        self.button1.pack()

    def _doit(self):
        self.button1.configure(text="Ouch, Not There!")

        self._add_passwords = tk.StringVar()
        self._add_phones = tk.StringVar()
        self._add_websites = tk.StringVar()

        self._add_passwords.set(False)
        self._add_phones.set(False)
        self._add_websites.set(False)

        c1 = tk.Checkbutton(text="Passwords", variable=self._add_passwords)
        c2 = tk.Checkbutton(text="Phones", variable=self._add_phones)
        c3 = tk.Checkbutton(text="Websites", variable=self._add_websites)

        self._selection = tk.StringVar()
        self._selection.set('location')  # default button

        r1 = tk.Radiobutton(text="Location",
                           value='location', variable=self._selection)
        r2 = tk.Radiobutton(text="Model",
                           value='model', variable=self._selection)
        r3 = tk.Radiobutton(text="Site",
                           value='site', variable=self._selection)
        r4 = tk.Radiobutton(text="Contact Info",
                           value='cinfo', variable=self._selection)

        for w in (c1, c2, c3, r1, r2, r3, r4):
            w.pack(anchor='w')

        b_quit = tk.Button(text="Quit", command=self.destroy)
        b_quit.pack()

    self.button2 = tk.Button(text="Holder", command=self._doit)
        self.button2.pack()

    def _doit(self):
        self.button2.configure(text="Holder is Ouchie!")

    def _open_file(self): pass

    def _save_file(self): pass

    def _save_file_as(self): pass

    def _cut(self): pass

    def _copy(self): pass

    def _paste(self): pass

if __name__ == '__main__':
    main()
=============================================================================

#Menu_one
label menu_one:
    call screen menu1

init python:
    style.tips_button.xminimum = 400

screen menu1:
# Show the background.
    add "images/blank2.jpg"

# Show the menu in the middle of the screen.
    vbox:
        style_group "prefs"
        xalign 0.5
        yalign 0.5

        textbutton _("1. LDAP Info") action Start()
        textbutton _("2. Other") action ShowMenu("other")
        textbutton _("3. Other Menu") action ShowMenu("other_menu")
        textbutton _("4. KA Servers") action ShowMenu("load")
        textbutton _("5. Preferences") action ShowMenu("preferences")
        textbutton _("Help") action Help()
        textbutton _("Return to Previous Menu") action ShowMenu("main_menu")
        textbutton _("Return") action Return()
        textbutton _("Quit") action Quit(confirm=False)

init -2:

# Make all the main menu buttons be the same size.
    style pref_button:
        size_group "pref"
        xalign 1.0
    return
