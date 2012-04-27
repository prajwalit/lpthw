""" Exercise 19 """

def cheese_and_crackers (cheese_count, boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "\n"

print "direct"
cheese_and_crackers(20, 30)

print "variables"
cheese_no = 40
crackers_no = 50
cheese_and_crackers(cheese_no, crackers_no)

print "math"
cheese_and_crackers(3+5, 7-3)

print "combine"
cheese_and_crackers(cheese_no + 1, crackers_no - 1)

