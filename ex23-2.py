a = 7832

def con():
	print a
	
def fudge():
	print a
	
con()
fudge()

def dumb_sentence(name = 'Tim', action = 'ate', item = 'tuna'):
	print name, action, item
	
dumb_sentence()
dumb_sentence('Peggy', 'likes', 'Pu')

dumb_sentence(item = 'Awesome')
dumb_sentence(action = 'Is')

def add_numbers(*args):
	total = 0
	for a in args:
		total += a
	print total
	
add_numbers(3)
add_numbers(3, 32)
add_numbers(3, 43, 5453, 354234, 463463)

def health_calculator(age, apple_ate, cigs_smoked):
	answer = (100-age) + apple_ate * 3.5 - cigs_smoked * 2
	print(answer)

tim_data = [27, 20, 0]

health_calculator(tim_data[0], tim_data[1], tim_data[2])
health_calculator(*tim_data)
