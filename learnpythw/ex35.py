from sys import exit


prompt = "> "


def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input(prompt).strip()

    amount_taken = 0
    try:
        amount_taken = int(choice)
    except ValueError:
        dead("That's...that's not a number...you must have lost your mind during your adventure.")

    if amount_taken < 50:
        print "Nice, you're not greedy. You win!"
        exit()
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"

    in_room = True
    bear_moved = False

    while in_room:
        options = "Take honey, taunt bear, "
        if not bear_moved:
            options += "or leave the room."
        else:
            options += "or open the door."
        print options

        choice = raw_input(prompt).strip()

        if "honey" in choice:
            dead("The bear looks at you and then tears your face off.")
        elif "leave" in choice:
            dead("The bear charges at you when you turn your back on it and bites your head off.")
        elif "taunt" in choice and not bear_moved:
            print "The bear moves toward you. What do you do now?"
            bear_moved = True
        elif "taunt" in choice and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif "open" in choice and bear_moved:
            gold_room()
        else:
            dead("What the heck were you trying to do??")


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever, stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input(prompt).strip()

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Great choice! That was extremely tasty.")
    else:
        dead("No sane person would do that. Way to embrace your insanity!")


def dead(why):
    print why, "Good job!"
    exit()


def start():
    print "You are in a dark room."
    print "There is a door to your right and left"
    print "Which one do you take?"

    choice = raw_input(prompt).strip()

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
