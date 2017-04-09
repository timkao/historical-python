import random

print random.choice("learnPython")
print random.choice(["JGood", "is", "a", "handsome", "boy"])
print random.choice(("Tuple", "List", "Dict"))  

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = random.sample(list, 5) 
print slice
print list 