"""Exercise 35"""

from sys import exit

def gold_room ():
    print "This room is full of gold. How much do you take?"

    next = raw_input ("> ")

    if "0" in next or "1" in next:
        how_much = int (next)
    else:
        dead ("Man, learn to type a number.")
    if how_much < 50:
        print "Nice. You're not greedy, you win!"
        exit (0)
    else:
        dead ("You greedy bastard!")

def bear_room ():
    print """
There's a bear here.
The bear has a bunch of honey.
The fat bear is in front of another door.
How are you going to move this bear?"""

    bear_moved = False
    while True:
        next = raw_input ("> ")

        if next == "take honey":
            dead ("The bear looks at you then pimp slaps your head off.")
        elif next == "taunt bear" and not bear_moved:
            print "Bear has moved from the door. You can go thro' it now."
            bear_moved = True
        elif next == "open door" and bear_moved:
            gold_room ()
        else:
            print "I got no idea what that means."


def cthulu_room ():
    print """
Here you see the great evil cthulu.
He, it, whatever stares at you and you go insane.
Do you flee for life or eat your head?"""

    next = raw_input ("> ")

    if "flee" in next:
        start ()
    elif "head" in next:
        dead ("Well, that was tasty!")
    else:
        cthulu_room ()

def dead (why):
    print why, "Good Job!"
    exit (0)

def start():
    print """
You're in a dark room.
There's a door to your right and left.
Which one do you take?"""

    next = raw_input ("> ")

    if next == "left":
        bear_room ()
    elif next == "right":
        cthulu_room ()
    else:
        dead ("You stumble around room until you starve.")

start()
