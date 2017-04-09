cars = 100
space_in_car = 4
drivers = 30
passengers = 90
cars_driven = drivers
car_not_driven = cars - drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", car_not_driven, "empty cars today."
print "we can transport", carpool_capacity, "people today."
print "we have", passengers, "to carpool today"
print "we need to put about", average_passengers_per_car, "in each car."

