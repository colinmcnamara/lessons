class MyStuff(object):
	def __init__(self):
		#set the tangerine variable into the class MyStuff
		self.tangerine = "And now a thousand years between"

	def apple(self):
		print "I AM CLASSY APPLES!"

# The instantiate function, looks for def statemetents to create empty objects
#	to place values into 
thing = MyStuff() 
thing.apple() 
print thing.tangerine

