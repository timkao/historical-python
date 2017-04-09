
# setting the variables
x = "there are %d type of people." % 10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s." % (binary, do_not) # 1st place

# print out x and y
print x
print y

# compare the difference between %s and %r
print "I said: %r" % x # 2nd place
print "I also said: '%s'" % y # 3rd place

# put one variable inside another variable by using %
hilarious = False
joke_evaluation = "Isn't that joke so funny!? %r"

print joke_evaluation % hilarious # 4th place

# combine two string variables by using +
w = "This is the left side of..."
e = "a string with a right side"

print w + e
