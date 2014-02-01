## Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
	pass
	genus = "Animal"
	blood = "Warm or cold"
	babies = "Living"
#	def genus(self):
#		self.name = name
#		print name

## Make a class Dog is-an Animal and has-a function called __init__ that takes self and name parameters
## set the variable name with the name of the object (self.)
class Dog(Animal):
	def __init__(self, name, breed):
		## ??
		## self.name gets the object name as a string
		self.name = name
		self.type = breed
		self.sound = "Woof"
	def announce(self):
		print "-" * 10
		print "I am an %s My name is %s and I go %s" % (self.genus ,self.name, self.sound)
		print "My blood is %s, and I have %s babies" % (self.blood, self.babies)

## Make a class Cat that is-an Animal and has-a function called__init__ that takes self and name parameters
## set the variable name with the name of the object (self.)
class Cat(Animal):
	def __init__(self, name):
		## self.name gets the object name as a string
		self.name = name
		self.sound = "Meow"
		super(Animal, self).__init__()
	def announce(self):
		print "-" * 10
		print "I am an %s My name is %s and I go %s" % (self.genus ,self.name, self.sound)
		print "My blood is %s, and I have %s babies" % (self.blood, self.babies)


## Make a class Person that takes self and name parameters and set the variable name with self. and to None
class Person(object):
	def __init__(self, name):
		## ??
		self.name = name

		## Person has-a pet of some kind
		self.pet = None
	def announce(self):
		print "-" * 10
		print "My name is %s I have a pet named %s that goes %s " % (self.name ,self.pet.name, self.pet.sound)
## Make a class Employee that is-a Person and has-a __init__ that takes parameters self, name and salary
## use a super to do wizardry  inside of the function
## set the variable salary as object.salary value
class Employee(Person):
	def __init__(self, name, salary):
		## ?? What is this strange magic
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## make a class fish 
class Fish(object):
	def __init__(self, name):
		## ??
		self.name = name	
	pass
	genus = "Animal"
	blood = "cold"
	babies = "Both living eggs"
	def announce(self):
		print "-" * 10
		print "My name is %s and I live in the %s " % (self.name, self.home)
		print "I am an %s I spawn in %s water and my flesh is %s" % (self.genus , self.spawn_water, self.flesh_color)
		print "My blood is %s, and I have %s babies" % (self.blood, self.babies)
		print "I have a %s shape" % (self.shape)
## make a class Salmon that is-a fish
class Salmon(Fish):
	pass
	def __init__(self, name, home):
		self.home = home
		self.name = name		
	spawn_water = "fresh"
	flesh_color = "pink"
	shape = "Torpedo"
#	def announce(self):
#		print "-" * 10
#		print "My name is %s and I live in the %s " % (self.name, self.home)
#		print "I am an %s I spawn in %s water and my flesh is %s" % (self.genus , self.spawn_water, self.flesh_color)
#		print "My blood is %s, and I have %s babies" % (self.blood, self.babies)
#		print "I have a %s shape" % (self.shape)
## make a calss Halibut that is-a fish
class Halibut(Fish):
	pass
	def __init__(self, name, home):
		self.home = home
		self.name = name
	spawn_water = "salt"
	flesh_color = "white"
	shape = "Flat"
#	def announce(self):
#		print "-" * 10
#		print "My name is %s and I live in the %s " % (self.name, self.home)
#		print "I am an %s I spawn in %s water and my flesh is %s" % (self.genus , self.spawn_water, self.flesh_color)
#		print "My blood is %s, and I have %s babies" % (self.blood, self.babies)
#		print "I have a %s shape" % (self.shape)
## object rover is-a dog with the name of rover
rover = Dog("Rover", "pug")

## object satan is-a cat with the name of satan
satan = Cat("Satan")

## mary is-a Person with the name of Mary
mary = Person("Mary")

## the value pet in the class object (class) mary is satan
mary.pet = satan

## the object frank is in the class employee and has the parameter frank (name) and the salary 120000 (salary) passed as values
frank = Employee("Frank", 120000 )

## the object frank has a value pet that is set as the object rover
frank.pet = rover

## the object flipper is-a fish
flipper = Fish("Flipper")

## the object crouse is-a salmon
crouse = Salmon("bob", "Rouge River")

## the object harry is-a Halibut
harry = Halibut("Harry", "Bering Sea")

print "Employee named %s makes %s" % (frank.name, frank.salary)
# procedural way of saying this
print "-" * 10
print "Procedural way of programming  "
print "My name is %s and I go %s" % (satan.name, satan.sound)
# better object oriented way of saying this
print "_" * 10 
print "Object Oriented Way of Programming"
satan.announce()
rover.announce()
mary.announce()
crouse.announce()
harry.announce()
