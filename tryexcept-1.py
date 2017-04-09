def temp_convert(var):
	try:
		return int(var)
	except ValueError, test:
		print "The arguement does not contain numbers\n", test
		
temp_convert("xyz")