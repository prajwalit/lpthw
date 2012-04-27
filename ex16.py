""" Exercise 16 """

from sys import argv

script, filename = argv

print "We're going to erase file %s." % filename
print "If you don't want that, hit Ctrl-C."
print "If you do want that, hit Return."

raw_input("?")

print "Opening a file..."
target = open(filename, "w")

print "Truncating the file."
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "Done."
target.close()
