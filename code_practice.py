def PrimeMover(num): 
	result = []
	n1 = 1
	n2 = 100
	while len(result) < int(num):
		for i in range(n1, n2+1):
			prime = []
			for j in range(1, i +1):
				if i % j == 0:
					prime.append(j)
				else:
					continue
			if len(prime) == 2:
				result.append(i)
			else:
				continue
		n2 += 100
		n1 += 100
	return result[int(num)-1]
		    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PrimeMover(raw_input())  