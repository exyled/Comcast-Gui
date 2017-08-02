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

##Main Menu Group 2 Buttons
    frame:
        style_group "mm"
        xalign .334
        yalign .00

        has vbox

        textbutton _("Unused 1") action ShowMenu("group2_button1")
        textbutton _("Unused 2") action ShowMenu("group2_button2")
        textbutton _("Unused 3") action ShowMenu("group2_button3")
        textbutton _("Unused 4") action ShowMenu("group2_button4")
        textbutton _("Unused 5") action ShowMenu("group2_button5")
        textbutton _("Unused 6") action ShowMenu("group2_button6")
        textbutton _("Unused 7") action ShowMenu("group2_button7")
        textbutton _("Unused 8") action ShowMenu("group2_button8")
        textbutton _("Unused 9") action ShowMenu("group2_button9")
        textbutton _("Unused 10") action ShowMenu("group2_button10")
        textbutton _("Unused 11") action ShowMenu("group2_button11")
        textbutton _("Unused 12") action ShowMenu("group2_button12")
        textbutton _("Unused 13") action ShowMenu("group2_button13")
        textbutton _("Unused 14") action ShowMenu("group2_button14")
        textbutton _("Unused 15") action ShowMenu("group2_button15")
        textbutton _("Unused 16") action ShowMenu("group2_button16")
        textbutton _("Unused 17") action ShowMenu("group2_button17")
        textbutton _("Unused 18") action ShowMenu("group2_button18")
        textbutton _("Unused 19") action ShowMenu("group2_button19")

##Main Menu Group 3 Buttons
    frame:
        style_group "mm"
        xalign .667
        yalign .00

        has vbox

        textbutton _("Unused 1") action ShowMenu("group3_button1")
        textbutton _("Unused 2") action ShowMenu("group3_button2")
        textbutton _("Unused 3") action ShowMenu("group3_button3")
        textbutton _("Unused 4") action ShowMenu("group3_button4")
        textbutton _("Unused 5") action ShowMenu("group3_button5")
        textbutton _("Unused 6") action ShowMenu("group3_button6")
        textbutton _("Unused 7") action ShowMenu("group3_button7")
        textbutton _("Unused 8") action ShowMenu("group3_button8")
        textbutton _("Unused 9") action ShowMenu("group3_button9")
        textbutton _("Unused 10") action ShowMenu("group3_button10")
        textbutton _("Unused 11") action ShowMenu("group3_button11")
        textbutton _("Unused 12") action ShowMenu("group3_button12")
        textbutton _("Unused 13") action ShowMenu("group3_button13")
        textbutton _("Unused 14") action ShowMenu("group3_button14")
        textbutton _("Unused 15") action ShowMenu("group3_button15")
        textbutton _("Unused 16") action ShowMenu("group3_button16")
        textbutton _("Unused 17") action ShowMenu("group3_button17")
        textbutton _("Unused 18") action ShowMenu("group3_button18")
        textbutton _("Unused 19") action ShowMenu("group3_button19")

##Main Menu Group 4 Buttons
    frame:
        style_group "mm"
        xalign .999
        yalign .00

        has vbox

        textbutton _("Unused 1") action ShowMenu("group4_button1")
        textbutton _("Unused 2") action ShowMenu("group4_button2")
        textbutton _("Unused 3") action ShowMenu("group4_button3")
        textbutton _("Unused 4") action ShowMenu("group4_button4")
        textbutton _("Unused 5") action ShowMenu("group4_button5")
        textbutton _("Unused 6") action ShowMenu("group4_button6")
        textbutton _("Unused 7") action ShowMenu("group4_button7")
        textbutton _("Unused 8") action ShowMenu("group4_button8")
        textbutton _("Unused 9") action ShowMenu("group4_button9")
        textbutton _("Unused 10") action ShowMenu("group4_button10")
        textbutton _("Unused 11") action ShowMenu("group4_button11")
        textbutton _("Unused 12") action ShowMenu("group4_button12")
        textbutton _("Unused 13") action ShowMenu("group4_button13")
        textbutton _("Unused 14") action ShowMenu("group4_button14")
        textbutton _("Unused 15") action ShowMenu("group4_button15")
        textbutton _("Unused 16") action ShowMenu("group4_button16")
        textbutton _("Unused 17") action ShowMenu("group4_button17")
        textbutton _("Unused 18") action ShowMenu("group4_button18")

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
# Navigation
# Screen that's included in other screens to display the game menu
# navigation and background.
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .99
        yalign .99

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"

##############################################################################
# Main Menu 2

screen main_menu_2():

    # This ensures that any other menu screen is replaced.
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

##############################################################################
# Main Menu 3
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu_3():

    # This ensures that any other menu screen is replaced.
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

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"

##############################################################################
# group1_button1 menu

screen group1_button1():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Create TarBall")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Export LDIF")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Import LDIF")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Option 4")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Option 5")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

        #The middle column
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Option 6")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                label _("Option 7")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Option 8")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Option 9")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Option 10")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        #Right column
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Option 11")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Option 12")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Option 13")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Option 14")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"


init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0

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