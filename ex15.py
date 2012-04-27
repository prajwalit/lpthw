""" Exercise 15 """

from sys import argv

script, filename = argv

text = open(filename)

print "Contents of %s are -" % filename
print text.read()
text.close()

print "I'll also ask you to type it again:"
filename = raw_input("> ")

text = open(filename)

print "Contents of %s are -" % filename
print text.read()
text.close()
