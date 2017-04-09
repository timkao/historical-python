def print_two(*args):
	print "%r" % (args,)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "I got nothing."
	
print_two("Tim", "Kao", "go", "go")
print_two_again("Tim","Kao")
print_one("Go!")
print_none()
