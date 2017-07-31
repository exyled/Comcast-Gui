import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
import sys

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        ##Menu System Works, as long as I keep it in the same class
        self.title("Comcast DemoBar")

        sampleapp = tk.Menu()

        # file menu
        file_menu = tk.Menu(sampleapp, tearoff=False)
        file_menu.add_command(label='Open...', command=self._open_file)
        file_menu.add_command(label='Save', command=self._save_file)
        file_menu.add_command(label='Save as...', command=self._save_file_as)
        file_menu.add_command(label='Quit', command=self.destroy)
        sampleapp.add_cascade(label="File", menu=file_menu)

        # edit menu
        edit_menu = tk.Menu(sampleapp, tearoff=False)
        edit_menu.add_command(label='Cut', command=self._cut)
        edit_menu.add_command(label='Copy', command=self._copy)
        edit_menu.add_command(label='Paste', command=self._paste)
        sampleapp.add_cascade(label="Edit", menu=edit_menu)

        self.config(menu=sampleapp)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
#If you find the concept of creating instance in a class confusing, or if different pages need different arguments
#during construction, you can explicitly call each class separately. The loop serves mainly to illustrate the point
#that each class is identical.
#For example, to create the classes individually you can remove the loop (for F in (StartPage, ...) with this:
        self.frames["StartPage"] = StartPage(parent=container, controller=self)
        self.frames["PageOne"] = PageOne(parent=container, controller=self)
        self.frames["PageOne_1"] = PageOne_1(parent=container, controller=self) #This Works
#        self.frames["PageOneSub1"] = PageOneSub1(parent=container, controller=self) # This Works as well
        self.frames["PageTwo"] = PageTwo(parent=container, controller=self)
#        self.frames["PageTwo_1"] = PageOne_1(parent=container, controller=self)
        self.frames["PageThree"] = PageThree(parent=container, controller=self)
#        self.frames["PageThree_1"] = PageOne_1(parent=container, controller=self)
        self.frames["PageFour"] = PageFour(parent=container, controller=self)
#        self.frames["PageFour_1"] = PageOne_1(parent=container, controller=self)
        self.frames["PageFive"] = PageFive(parent=container, controller=self)
#        self.frames["PageFive_1"] = PageOne_1(parent=container, controller=self)
        self.frames["PageSix"] = PageSix(parent=container, controller=self)
#        self.frames["PageSix_1"] = PageOne_1(parent=container, controller=self)
        self.frames["PageSeven"] = PageSeven(parent=container, controller=self)
#        self.frames["PageSeven_1"] = PageOne_1(parent=container, controller=self)
        self.frames["PageEight"] = PageEight(parent=container, controller=self)
#        self.frames["PageEight_1"] = PageOne_1(parent=container, controller=self)
        self.frames["PageNine"] = PageNine(parent=container, controller=self)
#        self.frames["PageNine_1"] = PageOne_1(parent=container, controller=self)

        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageOne"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageOne_1"].grid(row=0, column=0, sticky="nsew") #This Works
#        self.frames["PageOneSub1"].grid(row=0, column=0, sticky="nsew") # This Works as well
        self.frames["PageTwo"].grid(row=0, column=0, sticky="nsew")
#        self.frames["PageTwo_1"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageThree"].grid(row=0, column=0, sticky="nsew")
#        self.frames["PageThree_1"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageFour"].grid(row=0, column=0, sticky="nsew")
#        self.frames["PageFour_1"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageFive"].grid(row=0, column=0, sticky="nsew")
#        self.frames["PageFive_1"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageSix"].grid(row=0, column=0, sticky="nsew")
#        self.frames["PageSix_1"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageSeven"].grid(row=0, column=0, sticky="nsew")
#        self.frames["PageSeven_1"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageEight"].grid(row=0, column=0, sticky="nsew")
#        self.frames["PageEight_1"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageNine"].grid(row=0, column=0, sticky="nsew")
#        self.frames["PageNine_1"].grid(row=0, column=0, sticky="nsew")

#        for F in (StartPage, PageOne, PageTwo):
#            page_name = F.__name__
#            frame = F(parent=container, controller=self)
#            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
#            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def _open_file(self): pass

    def _save_file(self): pass

    def _save_file_as(self): pass

    def _cut(self): pass

    def _copy(self): pass

    def _paste(self): pass

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="1. Phone Manuals",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack()
        button2 = tk.Button(self, text="2. BVE Info",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.pack()
        button3 = tk.Button(self, text="3. Websites",
                            command=lambda: controller.show_frame("PageThree"))
        button3.pack()
        button4 = tk.Button(self, text="4. Walkthroughs",
                            command=lambda: controller.show_frame("PageFour"))
        button4.pack()
        button5 = tk.Button(self, text="5. Other Menu",
                            command=lambda: controller.show_frame("PageFive"))
        button5.pack()
        button6 = tk.Button(self, text="Go to Page Six",
                            command=lambda: controller.show_frame("PageSix"))
        button6.pack()
        button7 = tk.Button(self, text="Go to Page Seven",
                            command=lambda: controller.show_frame("PageSeven"))
        button7.pack()
        button8 = tk.Button(self, text="8. Help",
                            command=lambda: controller.show_frame("PageEight"))
        button8.pack()
        button9 = tk.Button(self, text="9. Preferences",
                            command=lambda: controller.show_frame("PageNine"))
        button9.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="1. Phone Manuals", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        button1 = tk.Button(self, text="1. Polycom Phones",
                            command=lambda: controller.show_frame("PageOne_1"))
        button1.pack()
#        button2 = tk.Button(self, text="2. Panasonic Phones",
#                            command=lambda: controller.show_frame("PageOne_2"))
#        button2.pack()
#        button3 = tk.Button(self, text="3. Websites",
#                            command=lambda: controller.show_frame("PageOne-3"))
#        button3.pack()
#        button4 = tk.Button(self, text="4. Walkthroughs",
#                            command=lambda: controller.show_frame("PageOne-4"))
#        button4.pack()
#        button5 = tk.Button(self, text="5. Other Menu",
#                            command=lambda: controller.show_frame("PageOne-5"))
#        button5.pack()
#        button6 = tk.Button(self, text="Go to Page Six",
#                            command=lambda: controller.show_frame("PageOne-6"))
#        button6.pack()
#        button7 = tk.Button(self, text="Go to Page Seven",
#                            command=lambda: controller.show_frame("PageOne-7"))
#        button7.pack()
#        button8 = tk.Button(self, text="8. Help",
#                            command=lambda: controller.show_frame("PageOne-8"))
#        button8.pack()
#        button9 = tk.Button(self, text="9. Preferences",
#                            command=lambda: controller.show_frame("PageOne-9"))
#        button9.pack()


class PageOne_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="1.1 Not Phone Manuals", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        button0 = tk.Button(self, text="Go Back One Page",
                           command=lambda: controller.show_frame("PageOne"))
        button0.pack()
        button1 = tk.Button(self, text="1. Polycom Phones",
                            command=lambda: controller.show_frame("PageOne1"))
        button1.pack()
        button2 = tk.Button(self, text="2. Panasonic Phones",
                            command=lambda: controller.show_frame("PageOne2"))
        button2.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageTwo_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()

#class PageThree_2(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        self.controller = controller
#        label = tk.Label(self, text="This is page 2", font=controller.title_font)
#        label.pack(side="top", fill="x", pady=10)
#        button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#        button.pack()

class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()

#class PageFour_2(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        self.controller = controller
#        label = tk.Label(self, text="This is page 2", font=controller.title_font)
#        label.pack(side="top", fill="x", pady=10)
#        button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#        button.pack()

class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()

#class PageFive_2(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        self.controller = controller
#        label = tk.Label(self, text="This is page 2", font=controller.title_font)
#        label.pack(side="top", fill="x", pady=10)
#        button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#        button.pack()

class PageSix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()

#class PageSix_2(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        self.controller = controller
#        label = tk.Label(self, text="This is page 2", font=controller.title_font)
#        label.pack(side="top", fill="x", pady=10)
#        button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#        button.pack()

class PageSeven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()

#class PageSeven_2(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        self.controller = controller
#        label = tk.Label(self, text="This is page 2", font=controller.title_font)
#        label.pack(side="top", fill="x", pady=10)
#        button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#        button.pack()

class PageEight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()

#class PageEight_2(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        self.controller = controller
#        label = tk.Label(self, text="This is page 2", font=controller.title_font)
#        label.pack(side="top", fill="x", pady=10)
#        button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#        button.pack()

class PageNine(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()


        b_quit = tk.Button(text="Quit", command=sys.exit)
        b_quit.pack()

#class PageNine_2(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        self.controller = controller
#        label = tk.Label(self, text="This is page 2", font=controller.title_font)
#        label.pack(side="top", fill="x", pady=10)
#        button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()