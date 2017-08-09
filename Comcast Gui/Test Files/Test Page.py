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

    def _open_file(self): pass

    def _save_file(self): pass

    def _save_file_as(self): pass

    def _cut(self): pass

    def _copy(self): pass

    def _paste(self): pass

if __name__ == '__main__':
    main()