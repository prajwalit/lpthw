"""Exercise 31"""

print "You enter in a dark room with two doors. Do you go thro dore #1 or #2?"

door = raw_input("> ")

if door == "1" or door == "#1":
    print "There's a giant bear here eating cheese cake. What do you do?"
    print "1. Take the cake." 
    print "2. Scream at bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Great Job!"
    elif bear == "2":
        print "The bear eats your legs off. Great Job!"
    else:
        print "Well doing %s is probably better. Bear runs away." % bear
        
elif door == "2" or door == "#2":
    print "You stare into endless abyss at Cthuhlu's ratina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by mind of jello. Great Job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Great Job!"
        
else:
    print "You stumble around and fall on a knife and die. Great Job!"
