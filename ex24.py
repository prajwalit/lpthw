""" Exercise 24 """

print 'I\'m prajwalit \\ I know \n New lines \n\t and Tabs'

poem = """
\tTing ting ting
ting tang ting
tang ting tang \n tang tang ting
\n\t\ttang tang tang
"""

print "----------"
print poem
print "----------"

five = 10 - 2 + 3 - 6
print "This should be five: %d" % five

def formula (started):
    jelly = started * 500
    jars = jelly / 1000
    crates = jars / 100
    return jelly, jars, crates

start = 10000
beans, jars, crates = formula (start)

print "Start: %d" % start
print "We'd have %d beans, %d jars, and %d crates" % (beans, jars, crates)

start /= 10

print "Start: %d" % start
print "We'd have %d beans, %d jars, and %d crates" % formula (start)

