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
