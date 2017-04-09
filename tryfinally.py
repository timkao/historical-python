try:
	fh = open("testfile", "w")
	fh.write("This is to test try and finally.")
finally:
	print "Error: Can\'t find file or read data"
	
	
try:
	fh = open("testfile", "r")
	try:
		fh.write("This is my testfile for exception handling!!")
	finally:
		print "Going to close the file!"
		fh.close()
except IOError:
	print "Error: can\'t find file or read data."
else:
	print "Correct!"