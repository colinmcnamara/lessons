i = 0
numbers = []

# while the variable i is less then 6
for i in range(0, 5):
	#print the number at the top of the list
	print "At the top i is %d" % i
	# append the list numbers w/ the contents of variable "i"
	numbers.append(i)
# increment "i" by one. could also use i += 1
#	i = i + 1
# print out numbers now : and then return the list numbers
	print "Numbers now: ", numbers
# print out the bottom of the list (this looks like a safety net to catch a endless loop)
	print "At the bottom i is %d" % i

# print to screen
print "The numbers: "

# loop through the numbers list. Assign each element to "num"
for num in numbers:
	#print out num (one stagement each for loop)
	print num
