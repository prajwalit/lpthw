"""Exercise 33"""

def counter (upto, step=1):
    count = 0
    numbers = []

    while count < upto:
        numbers.append (count)
        count += step
        
    print "Numbers:", numbers

counter (10)
