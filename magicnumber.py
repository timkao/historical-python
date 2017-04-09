magicnumber = 18

for n in range(101):
	if n is magicnumber:
		print "%d is the magicnumber!" % n
		break
	else:
		print n

answer = 0

while (answer < 100):
	if answer % 7 is 0:
		print answer
	answer += 1

numbersTaken = [2, 5, 12, 13, 17]

print "Here are the numbers that are still available"

for n in range(1,20):
	if n in numbersTaken:
		continue
	print n