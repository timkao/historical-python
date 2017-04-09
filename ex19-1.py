def cube(arg1, arg2, arg3):
	print "%.1f" % (arg1 * arg2 * arg3)
	
cube(3, 6, 9)
cube(3 + 3, 6 - 3, 9 / 3)

my_age = 32.0
my_height = 172.0

cube(3.0, 1.0, my_height / my_age)