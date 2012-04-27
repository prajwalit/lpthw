""" Exercise 21 """

def add (a, b):
    print "Adding %d and %d" % (a, b)
    return a + b

def subtract (a, b):
    print "Subtracting %d from %d" % (b, a)
    return a - b

def multiply (a, b):
    print "Multiplying %d and %d" % (a, b)
    return a * b

def divide (a, b):
    print "Dividing %d by %d" % (a, b)
    return a / b

print "Lets do some maths."

age = add (30, 5)
height = subtract (78, 4)
weight = multiply (90, 2)
iq = divide (100, 2)

print "Age: %d, height: %d, weight: %d, IQ: %d" % (age, height, weight, iq)

print "A Puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: %d" % what
