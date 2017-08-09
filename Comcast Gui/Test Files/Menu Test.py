import tkinter as tk
#Import filename' to import a python file into the script
import sys

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven, PageEight, PageNine):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Push Me Please Daddy!",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="LDAP Info",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = tk.Button(self, text="Visit Website",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()

        button4 = tk.Button(self, text="Other Menu",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack()

        button5 = tk.Button(self, text="KA Servers",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()

        button6 = tk.Button(self, text="Preferences",
                            command=lambda: controller.show_frame(PageSix))
        button6.pack()

        button7 = tk.Button(self, text="Help",
                            command=lambda: controller.show_frame(PageSeven))
        button7.pack()

        button8 = tk.Button(self, text="Return to Previous Menu",
                            command=lambda: controller.show_frame(PageEight))
        button8.pack()

        button9 = tk.Button(self, text="Quit 1",
                            command=lambda: controller.show_frame(PageNine))
        button9.pack()

#Not working for some reason, instead it goes to page nine
#        self.button10 = tk.Button(text="Quit 2", command=self._doit10)
#        self.button10.pack()
#
#    def _doit10(self):
#        self.button10.configure(text="Quit, You Wish!", command=self.destroy)

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageOne2))
        button2.pack()

        button3 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageOne3))
        button3.pack()

        button4 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageOne4))
        button4.pack()

        button5 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageOne5))
        button5.pack()

        button6 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageOne6))
        button6.pack()

        button7 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageOne7))
        button7.pack()

        button8 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageOne8))
        button8.pack()

        button9 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageOne9))
        button9.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo2))
        button2.pack()

        button3 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageTwo3))
        button3.pack()

        button4 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageTwo4))
        button4.pack()

        button5 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageTwo5))
        button5.pack()

        button6 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageTwo6))
        button6.pack()

        button7 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageTwo7))
        button7.pack()

        button8 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageTwo8))
        button8.pack()

        button9 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageTwo9))
        button9.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Three!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageThree2))
        button2.pack()

        button3 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageThree3))
        button3.pack()

        button4 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageThree4))
        button4.pack()

        button5 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageThree5))
        button5.pack()

        button6 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageThree6))
        button6.pack()

        button7 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageThree7))
        button7.pack()

        button8 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageThree8))
        button8.pack()

        button9 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageThree9))
        button9.pack()


class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Four!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageFour2))
        button2.pack()

        button3 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageFour3))
        button3.pack()

        button4 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageFour4))
        button4.pack()

        button5 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageFour5))
        button5.pack()

        button6 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageFour6))
        button6.pack()

        button7 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageFour7))
        button7.pack()

        button8 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageFour8))
        button8.pack()

        button9 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageFour9))
        button9.pack()


class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Five!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageFive2))
        button2.pack()

        button3 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageFive3))
        button3.pack()

        button4 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageFive4))
        button4.pack()

        button5 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageFive5))
        button5.pack()

        button6 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageFive6))
        button6.pack()

        button7 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageFive7))
        button7.pack()

        button8 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageFive8))
        button8.pack()

        button9 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageFive9))
        button9.pack()


class PageSix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Six!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageSix2))
        button2.pack()

        button3 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageSix3))
        button3.pack()

        button4 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageSix4))
        button4.pack()

        button5 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageSix5))
        button5.pack()

        button6 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageSix6))
        button6.pack()

        button7 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageSix7))
        button7.pack()

        button8 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageSix8))
        button8.pack()

        button9 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageSix9))
        button9.pack()


class PageSeven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Seven!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageSeven2))
        button2.pack()

        button3 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageSeven3))
        button3.pack()

        button4 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageSeven4))
        button4.pack()

        button5 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageSeven5))
        button5.pack()

        button6 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageSeven6))
        button6.pack()

        button7 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageSeven7))
        button7.pack()

        button8 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageSeven8))
        button8.pack()

        button9 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageSeven9))
        button9.pack()


class PageEight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Eight!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageEight2))
        button2.pack()

        button3 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageEight3))
        button3.pack()

        button4 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageEight4))
        button4.pack()

        button5 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageEight5))
        button5.pack()

        button6 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageEight6))
        button6.pack()

        button7 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageEight7))
        button7.pack()

        button8 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageEight8))
        button8.pack()

        button9 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageEight9))
        button9.pack()


class PageNine(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Nine!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageNine2))
        button2.pack()

        button3 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageNine3))
        button3.pack()

        button4 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageNine4))
        button4.pack()

        button5 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageNine5))
        button5.pack()

        button6 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageNine6))
        button6.pack()

        button7 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageNine7))
        button7.pack()

        button8 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageNine8))
        button8.pack()

        button9 = tk.Button(self, text="Holder",
                            command=lambda: controller.show_frame(PageNine9))
        button9.pack()
#    def _doit10(self):
#        self.button10.configure(text="Quit, You Wish!", command=self.destroy

#        b_quit = tk.Button(text="Quit", command=self.destroy)
#        b_quit.pack()

        b_quit = tk.Button(text="Quit", command=sys.exit)
        b_quit.pack()

app = SeaofBTCapp()
app.mainloop()