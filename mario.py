from sys import argv

script, tall = argv

height = int(tall) + 1

for i in range(1, height):
	
	j = i + 1
	k = height + 1 - j
	
	for k in range(0, k):
		print " ",
		
	for j in range(0, j):
		print "#",
	
	print "\n"
		
