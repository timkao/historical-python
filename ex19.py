# define how the cheese_and_crackers function works
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "you have %d cheeses!" % cheese_count
	print "you have %d boxes_of_crackers." % boxes_of_crackers
	print "Man, that's enought for a party!"
	print "Get a blanket.\n"

# we can type the numbers in
print "We can just give the function numbers directly."
cheese_and_crackers(20,30)

# we can put variables
print "Or, we could use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# we can do math inside the input
print "We can even do math inside too."
cheese_and_crackers(10 + 20, 5 + 6 )

# Variables can interact with numbers as well
print "And we can combine the two, variables and math."
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)