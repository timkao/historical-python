groceries = {'cereal', 'milk', 'starcrunch', 'beer', 'duck tape', 'lotion', 'beer'}
print groceries

if 'milk' in groceries:
	print "You already have milk hoss!"
else:
	print "oh yeah, you need milk!"
	
classmates = {'Tony': ' cool but smells', 'Emma': ' sits behind me', 'Lucy': ' ask too many questions'}

for k, v in classmates.items():
	print k + v