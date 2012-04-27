"""Exercise 29"""

people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats..."

if people > cats:
    print "Not many cats..."

if people < dogs:
    print "Too many dogs..."

if people > dogs:
    print "Phew..."

dogs += 5

if people >= dogs:
    print ">="

if people <= dogs:
    print "<="

if people == dogs:
    print "=="
