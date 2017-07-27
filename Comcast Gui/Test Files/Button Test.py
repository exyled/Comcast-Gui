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
        lab1.pack(padx=30, pady=5)
#Controls the width and Height of the MenuBar
# Main Menu is Here, Each points to the corresponding item under DEF
        self.button1 = tk.Button(text="Push Me Please Daddy!", command=self._doit)
        self.button1.pack()
        self.button2 = tk.Button(text="LDAP Info", command=self._doit2)
# action OpenTXT("/group1/button3/LDAP.txt")
        self.button2.pack()
        self.button3 = tk.Button(text="Visit Website", command=self._doit3)
# action OpenURL("http://google.com")
        self.button3.pack()
        self.button4 = tk.Button(text="Other Menu", command=self._doit4)
# action ShowMenu("other_menu")
        self.button4.pack()
        self.button5 = tk.Button(text="KA Servers", command=self._doit5)
# action ShowMenu("load")
        self.button5.pack()
        self.button6 = tk.Button(text="Preferences", command=self._doit6)
# action ShowMenu("preferences")
        self.button6.pack()
        self.button7 = tk.Button(text="Help", command=self._doit7)
# action Help()
        self.button7.pack()
        self.button8 = tk.Button(text="Return to Previous Menu", command=self._doit8)
# action ShowMenu("main_menu")
        self.button8.pack()
        self.button9 = tk.Button(text="Return", command=self._doit9)
# action Return()
        self.button9.pack()
        self.button10 = tk.Button(text="Quit", command=self._doit10)
# action Quit(confirm=False)
        self.button10.pack()

    def _doit(self):
        self.button1.configure(text="Ouch, Not There!")
    def _doit2(self):
        self.button2.configure(text="LDAP Not Here", ldap = open("LDAP.txt"))
        print(ldap.read())
# Need to add the Files to the Correct Directories for them to Open properly.
#        file_object = open("/group1/button3/LDAP.txt", “w”) where file_object is the variable to add the file= object.)
# Or as f = open = ("item.txt"[if in home dir])
#       print(f.read()) [shows the txt doc right on the screen]
    def _doit3(self):
        import webbrowser
# Imports the webbrowser function
        webbrowser.open('www.google.com', new=2)
# webbrowser.open('http://google.co.kr', new=2)  If new is 0, the url is opened in the same browser window if possible.
# If new is 1, a new browser window is opened if possible. If new is 2, a new browser page (“tab”) is opened if
# possible
# OLD-Stuff       self.button3.configure(text="Visit Website... NOT", webbrowser=open('www.google.com', new=2))
    def _doit4(self):
        self.button4.configure(text="Other Menu-Not For You")
#action ShowMenu("other_menu")
    def _doit5(self):
        self.button5.configure(text="KA Servers, Don't Exist")
#action ShowMenu("load")
    def _doit6(self):
        self.button6.configure(text="Preferences are Gone")
#action ShowMenu("preferences")
    def _doit7(self):
        self.button7.configure(text="Help Me Not")
#action Help()
    def _doit8(self):
        self.button8.configure(text="Return to Previous Menu, If You Dare")
#action ShowMenu("main_menu")
    def _doit9(self):
        self.button9.configure(text="Return to Nothing")
#action Return()
    def _doit10(self):
        self.button10.configure(text="Quit, You Wish!", command=self.destroy)
#        b_quit = tk.Button(text="Quit", command=self.destroy)
#        b_quit.pack()
#action Quit(text="", command=self.destroy)



#        self._add_passwords = tk.StringVar()
#        self._add_phones = tk.StringVar()
#        self._add_websites = tk.StringVar()
#
#        self._add_passwords.set(False)
#        self._add_phones.set(False)
#        self._add_websites.set(False)
#
#        c1 = tk.Checkbutton(text="Passwords", variable=self._add_passwords)
#        c2 = tk.Checkbutton(text="Phones", variable=self._add_phones)
#        c3 = tk.Checkbutton(text="Websites", variable=self._add_websites)
#
#        self._selection = tk.StringVar()
#        self._selection.set('location')  # default button
#
#        r1 = tk.Radiobutton(text="Location",
#                           value='location', variable=self._selection)
#        r2 = tk.Radiobutton(text="Model",
#                           value='model', variable=self._selection)
#        r3 = tk.Radiobutton(text="Site",
#                           value='site', variable=self._selection)
#        r4 = tk.Radiobutton(text="Contact Info",
#                           value='cinfo', variable=self._selection)
#
#        for w in (c1, c2, c3, r1, r2, r3, r4):
#            w.pack(anchor='w')

        b_quit = tk.Button(text="Quit", command=self.destroy)
        b_quit.pack()

    def _open_file(self): pass

    def _save_file(self): pass

    def _save_file_as(self): pass

    def _cut(self): pass

    def _copy(self): pass

    def _paste(self): pass

if __name__ == '__main__':
    main()
