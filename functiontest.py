def onelist():
	test = ["A", "B", 1, 3, "J"]
	return test

def checkA(test):
	for i in range(len(test)):
		if test[i] == "A":
			test[i] = 10000
		else:
			pass
			
def printd(test):
	print test
			
printd(test)
