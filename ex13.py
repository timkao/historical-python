from sys import argv

script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is ", first
print "Your second variable is ", second
print "Your third variable is ", third

test = raw_input("The %s is called? " % first)

print "The script is called: ", test 