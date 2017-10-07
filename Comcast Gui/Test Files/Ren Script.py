# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:
#label ldap:

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"


    menu:

        "... to ask her right away.":

            jump rightaway

        "... to ask her later.":

            jump later


label rightaway:

    show eileen happy

    e "Oh, hi, do we walk home together?"
    "I said and my voice was already shaking."

label later:

    return
