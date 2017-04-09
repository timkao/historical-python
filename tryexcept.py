try:
	fh = open("testfile", "r")
	fh.write("This is my testfile for exceptiong handling.")
except IOError:
	print "Error: can\'t find file or read data"
else:
	print "Written content in the file successfully."
	fh.close()
	
try:
	fh = open("testfile", "w")
	fh.write("This is my testfile for exceptiong handling.")
except IOError:
	print "Error: can\'t find file or read data"
else:
	print "Written content in the file successfully."
	fh.close()