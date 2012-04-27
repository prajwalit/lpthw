"""Exercise 30"""

people = 30
cars = 40
buses = 15

if cars > people:
    print "Take the cars."
elif cars < people:
    print "Don't take the cars."
else:
    print "Don't know then."


if buses > cars:
    print "Too many buses."
elif buses < cars:
    print "Take the buses."
else: 
    print "Still don't know."

if people > buses:
    print "Take the buses."
else:
    print "Stay home."
