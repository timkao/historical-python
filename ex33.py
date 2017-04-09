i = 0
n = 8
c = 2
numbers = []

while i < n:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i += c
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:
	print num