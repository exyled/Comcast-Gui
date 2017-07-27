#Group1_Button1
label group1_button1:
    call screen g1b1

init python:
    style.tips_button.xminimum = 400

screen g1b1:
# Show the background.
    add "images/blank2.jpg"

# Show the menu in the middle of the screen.
    vbox:
        style_group "prefs"
        xalign 0.5
        yalign 0.5

        textbutton _("LDAP Info") action OpenTXT("/group1/button3/LDAP.txt")
        textbutton _("Visit Website") action OpenURL("http://google.com")
        textbutton _("Other Menu") action ShowMenu("other_menu")
        textbutton _("KA Servers") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
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
