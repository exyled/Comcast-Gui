##Menubar and one button as well as the selection working together - 7-14-2017
import tkinter as tk
#Import filename' to import a python file into the script


#LARGE_FONT = ("Verdana", 12)
#
#
#class SeaofBTCapp(tk.Tk):
#    def __init__(self, *args, **kwargs):
#        tk.Tk.__init__(self, *args, **kwargs)
#        container = tk.Frame(self)
#
#        container.pack(side="top", fill="both", expand=True)
#
#        container.grid_rowconfigure(0, weight=1)
#        container.grid_columnconfigure(0, weight=1)
#
#        self.frames = {}
#
#        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven, PageEight, PageNine):
#            frame = F(container, self)
#
#            self.frames[F] = frame
#
#            frame.grid(row=0, column=0, sticky="nsew")
#
#        self.show_frame(StartPage)
#
#    def show_frame(self, cont):
#        frame = self.frames[cont]
#        frame.tkraise()
#
#
#class StartPage(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
#        label.pack(pady=10, padx=10)
#
#        button = tk.Button(self, text="Push Me Please Daddy!",
#                           command=lambda: controller.show_frame(PageOne))
#        button.pack()
#
#        button2 = tk.Button(self, text="LDAP Info",
#                            command=lambda: controller.show_frame(PageTwo))
#        button2.pack()
#
#        button3 = tk.Button(self, text="Visit Website",
#                            command=lambda: controller.show_frame(PageThree))
#        button3.pack()
#
#        button4 = tk.Button(self, text="Other Menu",
#                            command=lambda: controller.show_frame(PageFour))
#        button4.pack()
#
#        button5 = tk.Button(self, text="KA Servers",
#                            command=lambda: controller.show_frame(PageFive))
#        button5.pack()
#
#        button6 = tk.Button(self, text="Preferences",
#                            command=lambda: controller.show_frame(PageSix))
#        button6.pack()
#
#        button7 = tk.Button(self, text="Help",
#                            command=lambda: controller.show_frame(PageSeven))
#        button7.pack()
#
#        button8 = tk.Button(self, text="Return to Previous Menu",
#                            command=lambda: controller.show_frame(PageEight))
#        button8.pack()
#
#        button9 = tk.Button(self, text="Quit",
#                            command=lambda: controller.show_frame(PageNine))
#        button9.pack()
#
#
#class PageOne(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
#        label.pack(pady=10, padx=10)
#
#        button1 = tk.Button(self, text="Back to Home",
#                            command=lambda: controller.show_frame(StartPage))
#        button1.pack()
#
#        button2 = tk.Button(self, text="Page Two",
#                            command=lambda: controller.show_frame(PageOne2))
#        button2.pack()
#
#        button3 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageOne3))
#        button3.pack()
#
#        button4 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageOne4))
#        button4.pack()
#
#        button5 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageOne5))
#        button5.pack()
#
#        button6 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageOne6))
#        button6.pack()
#
#        button7 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageOne7))
#        button7.pack()
#
#        button8 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageOne8))
#        button8.pack()
#
#        button9 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageOne9))
#        button9.pack()
#
#
#class PageTwo(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
#        label.pack(pady=10, padx=10)
#
#        button1 = tk.Button(self, text="Back to Home",
#                            command=lambda: controller.show_frame(StartPage))
#        button1.pack()
#
#        button2 = tk.Button(self, text="Page Two",
#                            command=lambda: controller.show_frame(PageTwo2))
#        button2.pack()
#
#        button3 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageTwo3))
#        button3.pack()
#
#        button4 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageTwo4))
#        button4.pack()
#
#        button5 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageTwo5))
#        button5.pack()
#
#        button6 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageTwo6))
#        button6.pack()
#
#        button7 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageTwo7))
#        button7.pack()
#
#        button8 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageTwo8))
#        button8.pack()
#
#        button9 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageTwo9))
#        button9.pack()
#
#
#class PageThree(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
#        label.pack(pady=10, padx=10)
#        button1 = tk.Button(self, text="Back to Home",
#                            command=lambda: controller.show_frame(StartPage))
#        button1.pack()
#
#        button2 = tk.Button(self, text="Page Two",
#                            command=lambda: controller.show_frame(PageThree2))
#        button2.pack()
#
#        button3 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageThree3))
#        button3.pack()
#
#        button4 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageThree4))
#        button4.pack()
#
#        button5 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageThree5))
#        button5.pack()
#
#        button6 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageThree6))
#        button6.pack()
#
#        button7 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageThree7))
#        button7.pack()
#
#        button8 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageThree8))
#        button8.pack()
#
#        button9 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageThree9))
#        button9.pack()
#
#
#class PageFour(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
#        label.pack(pady=10, padx=10)
#
#        button1 = tk.Button(self, text="Back to Home",
#                            command=lambda: controller.show_frame(StartPage))
#        button1.pack()
#
#        button2 = tk.Button(self, text="Page Two",
#                            command=lambda: controller.show_frame(PageFour2))
#        button2.pack()
#
#        button3 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageFour3))
#        button3.pack()
#
#        button4 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageFour4))
#        button4.pack()
#
#        button5 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageFour5))
#        button5.pack()
#
#        button6 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageFour6))
#        button6.pack()
#
#        button7 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageFour7))
#        button7.pack()
#
#        button8 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageFour8))
#        button8.pack()
#
#        button9 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageFour9))
#        button9.pack()
#
#
#class PageFive(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
#        label.pack(pady=10, padx=10)
#
#        button1 = tk.Button(self, text="Back to Home",
#                            command=lambda: controller.show_frame(StartPage))
#        button1.pack()
#
#        button2 = tk.Button(self, text="Page Two",
#                            command=lambda: controller.show_frame(PageFive2))
#        button2.pack()
#
#        button3 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageFive3))
#        button3.pack()
#
#        button4 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageFive4))
#        button4.pack()
#
#        button5 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageFive5))
#        button5.pack()
#
#        button6 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageFive6))
#        button6.pack()
#
#        button7 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageFive7))
#        button7.pack()
#
#        button8 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageFive8))
#        button8.pack()
#
#        button9 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageFive9))
#        button9.pack()
#
#
#class PageSix(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
#        label.pack(pady=10, padx=10)
#
#        button1 = tk.Button(self, text="Back to Home",
#                            command=lambda: controller.show_frame(StartPage))
#        button1.pack()
#
#        button2 = tk.Button(self, text="Page Two",
#                            command=lambda: controller.show_frame(PageSix2))
#        button2.pack()
#
#        button3 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageSix3))
#        button3.pack()
#
#        button4 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageSix4))
#        button4.pack()
#
#        button5 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageSix5))
#        button5.pack()
#
#        button6 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageSix6))
#        button6.pack()
#
#        button7 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageSix7))
#        button7.pack()
#
#        button8 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageSix8))
#        button8.pack()
#
#        button9 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageSix9))
#        button9.pack()
#
#
#class PageSeven(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
#        label.pack(pady=10, padx=10)
#
#        button1 = tk.Button(self, text="Back to Home",
#                            command=lambda: controller.show_frame(StartPage))
#        button1.pack()
#
#        button2 = tk.Button(self, text="Page Two",
#                            command=lambda: controller.show_frame(PageSeven2))
#        button2.pack()
#
#        button3 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageSeven3))
#        button3.pack()
#
#        button4 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageSeven4))
#        button4.pack()
#
#        button5 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageSeven5))
#        button5.pack()
#
#        button6 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageSeven6))
#        button6.pack()
#
#        button7 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageSeven7))
#        button7.pack()
#
#        button8 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageSeven8))
#        button8.pack()
#
#        button9 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageSeven9))
#        button9.pack()
#
#
#class PageEight(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
#        label.pack(pady=10, padx=10)
#
#        button1 = tk.Button(self, text="Back to Home",
#                            command=lambda: controller.show_frame(StartPage))
#        button1.pack()
#
#        button2 = tk.Button(self, text="Page Two",
#                            command=lambda: controller.show_frame(PageEight2))
#        button2.pack()
#
#        button3 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageEight3))
#        button3.pack()
#
#        button4 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageEight4))
#        button4.pack()
#
#        button5 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageEight5))
#        button5.pack()
#
#        button6 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageEight6))
#        button6.pack()
#
#        button7 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageEight7))
#        button7.pack()
#
#        button8 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageEight8))
#        button8.pack()
#
#        button9 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageEight9))
#        button9.pack()
#
#
#class PageNine(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
#        label.pack(pady=10, padx=10)
#
#        button1 = tk.Button(self, text="Back to Home",
#                            command=lambda: controller.show_frame(StartPage))
#        button1.pack()
#
#        button2 = tk.Button(self, text="Page Two",
#                            command=lambda: controller.show_frame(PageNine2))
#        button2.pack()
#
#        button3 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageNine3))
#        button3.pack()
#
#        button4 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageNine4))
#        button4.pack()
#
#        button5 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageNine5))
#        button5.pack()
#
#        button6 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageNine6))
#        button6.pack()
#
#        button7 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageNine7))
#        button7.pack()
#
#        button8 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageNine8))
#        button8.pack()
#
#        button9 = tk.Button(self, text="Holder",
#                            command=lambda: controller.show_frame(PageNine9))
#        button9.pack()
#
#
#app = SeaofBTCapp()
#app.mainloop()


##############
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
