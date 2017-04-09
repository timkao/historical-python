print "how old are you?",
age = raw_input()
print "how tall are you?",
height = float(raw_input())
print "how much do you weight?",
weight = float(raw_input())

print "So you are %r old, %r tall, and %r heavy." % (age, height, weight)
print "your weight/height is %.1f" % (weight/height)

test = raw_input("give me something to do testing!\n")
print "I just type %s" % test