class Animal(object):
	
	blood = 30
	
	def __init__(self, name):
		self.name = name
		
	def wanwan(self):
		print "My name is %s" % self.name
	


class Dog(Animal):

	def __init__(self, name):
		self.name = name
	
	def bark(self):
		print "bark!"
	
class Cat(Animal):

	def __init__(self, name):
		self.name = name
		
class Person(object):

	def __init__(self, name):
		self.name = name
		self.pet = None
		
class Employee(Person):

	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary
		
class Fish(object):
	pass
	
class Salmon(Fish):
	pass
	
class Halibut(Fish):
	pass
	
rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()

print rover.bark()
print rover.blood
print rover.name
print frank.pet.bark()
print rover.wanwan()