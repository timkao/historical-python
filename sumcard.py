

def sumcard(yourcard):
	for i  in range(0, len(yourcard)):
	
		if yourcard[i] == "J" or yourcard[i] == "Q" or yourcard [i] == "K":
			yourcard[i] = 10
		else:
			pass

	yourcard.sort()
	if yourcard.count("A") == 2:
		yourcard[-2] = 1
	elif yourcard.count("A") == 3:
		yourcard[-2] = 1
		yourcard[-3] = 1
	elif yourcard.count("A") == 4:
		yourcard[-2] = 1
		yourcard[-3] = 1
		yourcard[-4] = 1
		
	if yourcard.count("A") == 0:
	
		x = 0	
	
		for j in range(0, len(yourcard)):	
			x = x + yourcard[j]
	
		return x
	
	elif yourcard.count("A") == 1:
	
		x1 = 0
	
		for k in range(0, len(yourcard) - 1):
			x1 = x1 + yourcard[k]
	
		if x1 <= 10:
			x1sum = x1 + 11
			return x1sum
		else:
			x1sum = x1 + 1
			return x1sum
		
	else:
		pass


