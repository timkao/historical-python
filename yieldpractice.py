
	
def h():
	print "To be brave"
	f = yield 5
	print f
	s = yield 12
	print "We are together!"
	
c = h()
first_yield = c.next()
second_yield = c.send("Fighting!")
print "check this", first_yield, second_yield