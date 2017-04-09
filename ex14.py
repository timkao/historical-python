from sys import argv

script, user_name, spouse = argv
start = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
like = raw_input(start)

print "Is %s your wife?" % spouse
wife = raw_input(start)

print "Where do you live %s?" % user_name
lives = raw_input(start)

print "What kind of computer do you have?"
computer = raw_input(start)

print """Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And %r your wife is her. You have a %r computer. Nice.""" % (like, lives, wife, computer)

