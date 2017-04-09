def functionName(level):
	if level < 2:
		raise "Invalid level!", level
	else:
		print "good level!"

try:		
	level = 3
	functionName(level)
except "Invalid level!":
	print "The level should be bigger than zero!"
else:
	print "Great!"
	
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
	  
try:
   raise Networkerror("Bad hostname")
except Networkerror,e:
   print e.args