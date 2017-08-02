import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
import sys
import os
import webbrowser

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        ##Menu System Works, as long as I keep it in the same class
        self.title("Comcast GuiBar") #The Title that shows on the MenuBar

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
        self.frames["PageThree_1"] = PageThree_1(parent=container, controller=self)
        self.frames["PageThree_2"] = PageThree_2(parent=container, controller=self)
        self.frames["PageThree_3"] = PageThree_3(parent=container, controller=self)
        self.frames["PageThree_4"] = PageThree_4(parent=container, controller=self)
        self.frames["PageThree_5"] = PageThree_5(parent=container, controller=self)
        self.frames["PageThree_6"] = PageThree_6(parent=container, controller=self)
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

        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew") #If I change the Row and Column then I can make
        # additional pages appear beside the current page
        self.frames["PageOne"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageOne_1"].grid(row=0, column=0, sticky="nsew") #This Works
#        self.frames["PageOneSub1"].grid(row=0, column=0, sticky="nsew") # This Works as well
        self.frames["PageTwo"].grid(row=0, column=0, sticky="nsew")
#        self.frames["PageTwo_1"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageThree"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageThree_1"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageThree_2"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageThree_3"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageThree_4"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageThree_5"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageThree_6"].grid(row=0, column=0, sticky="nsew")

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
        label = tk.Label(self, text="1.1 VVX Manuals", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        button0 = tk.Button(self, text="Go Back One Page",
                           command=lambda: controller.show_frame("PageOne"))
        button0.pack()
        button1 = tk.Button(self, text="1. VVX310 UserGuide",
                            command=lambda: os.startfile("..\Comcast Gui\Files\PhoneManuals\VVX310\VVX310_UserGuide.pdf")) #Works like it is supposed to.
                            #(OLD CODE)controller.show_frame("PageOne1"))
        button1.pack()
        button2 = tk.Button(self, text="2. VVX400 UserGuide",
                            command=lambda: os.startfile("..\Comcast Gui\Files\PhoneManuals\VVX400\VVX400_UserGuide.pdf")) #Works like it is supposed to.
        button2.pack()
        button3 = tk.Button(self, text="1. VVX500 UserGuide",
                            command=lambda: os.startfile("..\Comcast Gui\Files\PhoneManuals\VVX500\VVX500_UserGuide.pdf")) #Works like it is supposed to.
        button3.pack()
        button4 = tk.Button(self, text="1. VVX500 Admin",
                            command=lambda: os.startfile("..\Comcast Gui\Files\PhoneManuals\VVX500\VVX500_Admin.pdf")) #Works like it is supposed to.
        button4.pack()
        button5 = tk.Button(self, text="1. VVX500 QuickGuide",
                            command=lambda: os.startfile("..\Comcast Gui\Files\PhoneManuals\VVX500\VVX500_QuickGuide.pdf")) #Works like it is supposed to.
        button5.pack()
        button6 = tk.Button(self, text="1. VVX550 Admin",
                            command=lambda: os.startfile("..\Comcast Gui\Files\PhoneManuals\VVX500\VVX550_Admin.pdf")) #Works like it is supposed to.
        button6.pack()
        button7 = tk.Button(self, text="1. VVX600 UserGuide",
                            command=lambda: os.startfile("..\Comcast Gui\Files\PhoneManuals\VVX600\VVX600_UserGuide.pdf")) #Works like it is supposed to.
        button7.pack()
        button8 = tk.Button(self, text="1. Conference Phone 6000",
                            command=lambda: os.startfile("..\Comcast Gui\Files\PhoneManuals\IP6000_UserGuide.pdf")) #Works like it is supposed to.
        button8.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="2. BVE Info", font=controller.title_font)
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
        button0 = tk.Button(self, text="Go Back One Page",
                           command=lambda: controller.show_frame("PageTwo"))
        button0.pack()

class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="3. Websites", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()
        button1 = tk.Button(self, text="1. BVE Websites",
                            command=lambda: controller.show_frame("PageThree_1"))
        button1.pack()
        button2 = tk.Button(self, text="2. SMB Websites",
                            command=lambda: controller.show_frame("PageThree_2"))
        button2.pack()
        button3 = tk.Button(self, text="3. Metro Websites",
                            command=lambda: controller.show_frame("PageThree_3"))
        button3.pack()
        button4 = tk.Button(self, text="4. Pri/Trunking Websites",
                            command=lambda: controller.show_frame("PageThree_4"))
        button4.pack()
        button5 = tk.Button(self, text="5. Customer Websites",
                            command=lambda: controller.show_frame("PageThree_5"))
        button5.pack()
        button6 = tk.Button(self, text="6. Other Websites",
                            command=lambda: controller.show_frame("PageThree_6"))
        button6.pack()

class PageThree_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="BVE WebSites", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()
###---BVE---
##WEB TOP - https://bve.comcast.com/portal-91/
        button0 = tk.Button(self, text="Go to WebTop",
                           command=lambda: webbrowser.open('https://bve.comcast.com/portal-91/', new=2))
        button0.pack()
###BVE Care Portal - https://voiceedgecare.comcast.com/
        button1 = tk.Button(self, text="Go to BVE Care Portal",
                           command=lambda: webbrowser.open('https://voiceedgecare.comcast.com/', new=2))
        button1.pack()
###Customer BVE Portal - https://voiceedge.comcast.com/
        button2 = tk.Button(self, text="Go to Customer BVE Portal",
                           command=lambda: webbrowser.open('https://voiceedge.comcast.com/', new=2))
        button2.pack()
###BVE/NGT Doc Portal - http://business.comcast.com/getstarted
        button3 = tk.Button(self, text="Go to BVE/NGT Doc Portal",
                           command=lambda: webbrowser.open('http://business.comcast.com/getstarted', new=2))
        button3.pack()
###Netxusa - https://www.netxusa.com/
        button4 = tk.Button(self, text="Go to Netxusa",
                           command=lambda: webbrowser.open('https://www.netxusa.com/', new=2))
        button4.pack()
###EdgeView - http://ev01.b.comcast.net/menu.html
        button5 = tk.Button(self, text="Go to EdgeView",
                           command=lambda: webbrowser.open('http://ev01.b.comcast.net/menu.html', new=2))
        button5.pack()
###AS07 - https://bve-web.wdv.comcast.net/Login/
        button6 = tk.Button(self, text="Go to AS07/08/10",
                           command=lambda: webbrowser.open('https://bve-web.wdv.comcast.net/Login/', new=2))
        button6.pack()
###SNAP - http://www.snaprecordings.com/
        button7 = tk.Button(self, text="Go to SNAP",
                           command=lambda: webbrowser.open('http://www.snaprecordings.com/', new=2))
        button7.pack()
###BVE RMA - https://wiki.io.comcast.net/download/attachments/166921705/BVE+RMA+Device+Ordering+Procedures.pdf?version=1&modificationDate=1369256532000
        button8 = tk.Button(self, text="Go to BVE RMA",
                           command=lambda: webbrowser.open('https://wiki.io.comcast.net/download/attachments/166921705/BVE+RMA+Device+Ordering+Procedures.pdf?version=1&modificationDate=1369256532000', new=2))
        button8.pack()
###Neustar - https://numbering.neustar.biz/secure
        button9 = tk.Button(self, text="Go to Neustar",
                           command=lambda: webbrowser.open('https://numbering.neustar.biz/secure', new=2))
        button9.pack()
###OrderPath - http://orderpath.comcast.net/op00/Logon
        button10 = tk.Button(self, text="Go to OrderPath",
                           command=lambda: webbrowser.open('http://orderpath.comcast.net/op00/Logon', new=2))
        button10.pack()
###Targus - https://webapp2.targusinfo.com/Authentication/login.aspx?ReturnUrl=%2fextranetmenu%2fdefault.aspx
        button11 = tk.Button(self, text="Go to Targus",
                           command=lambda: webbrowser.open('https://webapp2.targusinfo.com/Authentication/login.aspx?ReturnUrl=%2fextranetmenu%2fdefault.aspx', new=2))
        button11.pack()
#=======BVE DONE=======
###
class PageThree_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="SMB WebSites", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()
        button0 = tk.Button(self, text="Go Back One Page",
                           command=lambda: controller.show_frame("PageThree"))
        button0.pack()
###---SMB---
#        button1 = tk.Button(self, text="Go to ",
#                           command=lambda: webbrowser.open('www.google.com', new=2))
#        button1.pack()
#=======DONE=======
###
class PageThree_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Metro WebSites", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()
        button0 = tk.Button(self, text="Go Back One Page",
                           command=lambda: controller.show_frame("PageThree"))
        button0.pack()
###---Metro---
###CCOM - http://ccom/Diagram.aspx?ID=1
#        button1 = tk.Button(self, text="Go to ",
#                           command=lambda: webbrowser.open('www.google.com', new=2))
#        button1.pack()
###METRO E Lookup - http://metroe.comcast.net/view_sur_customers.php
#        button1 = tk.Button(self, text="Go to ",
#                           command=lambda: webbrowser.open('www.google.com', new=2))
#        button1.pack()
###Oracle Content - https://ucm.cable.comcast.com:16201/cs/login/login.htm
#        button1 = tk.Button(self, text="Go to ",
#                           command=lambda: webbrowser.open('www.google.com', new=2))
#        button1.pack()
###Century - https://century/cm or https://century.comcast.com/cm
#        button1 = tk.Button(self, text="Go to ",
#                           command=lambda: webbrowser.open('www.google.com', new=2))
#        button1.pack()
###CCS Tools MetroE - http://ccstools.comcast.net/ccsprovision/
#        button1 = tk.Button(self, text="Go to ",
#                           command=lambda: webbrowser.open('www.google.com', new=2))
#        button1.pack()
###EoHFC - http://cmts.comcast.net/view_eohfc_modems.php
#        button1 = tk.Button(self, text="Go to ",
#                           command=lambda: webbrowser.open('www.google.com', new=2))
#        button1.pack()
###=======DONE=======
###
class PageThree_4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pri/Trunking WebSites", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()
        button0 = tk.Button(self, text="Go Back One Page",
                           command=lambda: controller.show_frame("PageThree"))
        button0.pack()
###---Pri/Trunking---
###MSP/ADTRAN - http://msp01.b.comcast.net/al/secure/bin/index.html
#        button1 = tk.Button(self, text="Go to MSP/ADTRAN",
#                           command=lambda: webbrowser.open('http://msp01.b.comcast.net/al/secure/bin/index.html', new=2))
#        button1.pack()
###Device Lookup/NTETO - https://nccm.cm.comcast.net/login?next=/device-lookup/
#        button2 = tk.Button(self, text="Go to Device Lookup/NTETO",
#                           command=lambda: webbrowser.open('https://nccm.cm.comcast.net/login?next=/device-lookup/', new=2))
#        button2.pack()
###DRW Tool - http://icp.comcast.net/drw/index.cfm
#        button3 = tk.Button(self, text="Go to DRW Tool",
#                           command=lambda: webbrowser.open('http://icp.comcast.net/drw/index.cfm', new=2))
#        button3.pack()
###Scout - http://scoutmonitoring.g.comcast.net/network_monitoring/servlet/network_monitoring
#        button4 = tk.Button(self, text="Go to Scout",
#                           command=lambda: webbrowser.open('http://scoutmonitoring.g.comcast.net/network_monitoring/servlet/network_monitoring', new=2))
#        button4.pack()
###BACC - http://comcastbaccgui.comcast.net/bacc/jsp/bacclogin.jsp
#        button5 = tk.Button(self, text="Go to BACC",
#                           command=lambda: webbrowser.open('http://comcastbaccgui.comcast.net/bacc/jsp/bacclogin.jsp', new=2))
#        button5.pack()
###AS03 - https://bvtrunking-web.wdv.comcast.net/Login/
#        button6 = tk.Button(self, text="Go to AS03",
#                           command=lambda: webbrowser.open('https://bvtrunking-web.wdv.comcast.net/Login/', new=2))
#        button6.pack()
###AS04 - https://web01.wdv.comcast.net/Login/
#        button7 = tk.Button(self, text="Go to AS04",
#                           command=lambda: webbrowser.open('https://web01.wdv.comcast.net/Login/', new=2))
#        button7.pack()
###AS05 - https://bvtrunking-web.wdv.comcast.net/Login/
#        button8 = tk.Button(self, text="Go to AS05",
#                           command=lambda: webbrowser.open('https://bvtrunking-web.wdv.comcast.net/Login/', new=2))
#        button8.pack()
###AS06 - https://web01.wdv.comcast.net/Login/
#        button9 = tk.Button(self, text="Go to AS06",
#                           command=lambda: webbrowser.open('https://web01.wdv.comcast.net/Login/', new=2))
#        button9.pack()
###AS07 - https://bve-web.wdv.comcast.net/Login/
#        button10 = tk.Button(self, text="Go to AS07/08/11",
#                           command=lambda: webbrowser.open('https://bve-web.wdv.comcast.net/Login/', new=2))
#        button10.pack()
###OrderPath - http://orderpath.comcast.net/op00/Logon
#        button11 = tk.Button(self, text="Go to OrderPath",
#                           command=lambda: webbrowser.open('http://orderpath.comcast.net/op00/Logon', new=2))
#        button11.pack()
###TNLocator - http://172.30.113.213/BCV_TNLocator.cfm
#        button12 = tk.Button(self, text="Go to TNLocator",
#                           command=lambda: webbrowser.open('http://172.30.113.213/BCV_TNLocator.cfm', new=2))
#        button12.pack()
###Broad Soft Disco - http://bcv.comcast.net/Disco/BSDisco.cfm
#        button13 = tk.Button(self, text="Go to Broad Soft Disco",
#                           command=lambda: webbrowser.open('http://bcv.comcast.net/Disco/BSDisco.cfm', new=2))
#        button13.pack()
###Broadsoft ILD Control - http://bcv.comcast.net/ILD/ILD_Control.cfm
#        button14 = tk.Button(self, text="Go to Broadsoft ILD Control",
#                           command=lambda: webbrowser.open('http://bcv.comcast.net/ILD/ILD_Control.cfm', new=2))
#        button14.pack()
###=======Pri/Trunking DONE=======
###
class PageThree_5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Customer WebSites", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()
        button0 = tk.Button(self, text="Go Back One Page",
                           command=lambda: controller.show_frame("PageThree"))
        button0.pack()
#---Customer---
#IPControl - http://incontrol.comcast.net/incontrol/logon.action
#IP Chicken - http://www.ipchicken.com/
#Network-Tools - http://network-tools.com/default.asp?prog=express&host=207.46.33.82
#Mac/Domain/IP Checker - http://www.techzoom.net/tools/networking.en
#DNS/IP/MX/Blacklists - http://www.mxtoolbox.com/DNSLookup.aspx
#E-mail Black List Removal - http://postmaster.comcast.net/index.html
#Coffer Mac Lookup - http://www.coffer.com/mac_find/
#MAC/IP to Hostname/HostnameIP - http://aruljohn.com/track.pl
#ESD Consule - https://esdconsole.g.cable.comcast.com/
#SMC Password - http://teamcentral/cdbs/cc/Main%20Page/Sub%20HTML%20Files/POD%20Page.html
#Email IPhone - http://businesshelp.comcast.com/Pages/HelpNFC.aspx?id=comcast-business-class-email
#IPAT - http://ipat.cable.comcast.com/ModemManagement/
#=======DONE=======
###
class PageThree_6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Other WebSites", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()
        button0 = tk.Button(self, text="Go Back One Page",
                           command=lambda: controller.show_frame("PageThree"))
        button0.pack()
#---Other---
#
#=======DONE=======
###
class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="4. Feature Walkthroughs", font=controller.title_font)
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
#        button0 = tk.Button(self, text="Go Back One Page",
#                           command=lambda: controller.show_frame("PageFour"))
#        button0.pack()

class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="5. Other Menu", font=controller.title_font)
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
#        button0 = tk.Button(self, text="Go Back One Page",
#                           command=lambda: controller.show_frame("PageFive"))
#        button0.pack()

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
#        button0 = tk.Button(self, text="Go Back One Page",
#                           command=lambda: controller.show_frame("PageSix"))
#        button0.pack()

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
#        button0 = tk.Button(self, text="Go Back One Page",
#                           command=lambda: controller.show_frame("PageSeven"))
#        button0.pack()

class PageEight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="8. Help", font=controller.title_font)
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
#        button0 = tk.Button(self, text="Go Back One Page",
#                           command=lambda: controller.show_frame("PageEight"))
#        button0.pack()

class PageNine(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="9. Preferences", font=controller.title_font)
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
#        button0 = tk.Button(self, text="Go Back One Page",
#                           command=lambda: controller.show_frame("PageNine"))
#        button0.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()