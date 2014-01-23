people = 10
cars = 30
buses = 10

#evaluate if cars are greater than people
if cars > people:
#print to screen
	print "We should take cars"
#if cars are not greater than people, evaluate if cars are less than people
elif cars < people:
#print to screen	
	print "We should not take cars."
#if neither of the above is true, print we can't decide
else:
#print to screen
	print "We can't decide."

#evaluate if busses are greater than cars
if buses > cars:
#print to screen
	print "That's to many buses."
# if the first statement is not true, evaluate if busses are less then cars
elif buses < cars:
#print to screen
	print "Maybe we should take the buses."
#if neither is true, print to screen "We still can't decide" 
else: 
	print "we still can't decide."
# evaluate if people are greater then buses
if people > buses:
#print to screen
	print "Alright, let's just take the buses."
# if the first statement is not true, then print to screen
else:
# print to screen
	print "Fine, let's stay home then."
#evaluate if people are equal to cars
if people == cars: 
#if that is true, print we have the same number of people as cards
	print "Wow, we have the same number of people as cars"
#evaluate if the first statement is not true
else:
#print a star wars refrence to screen
	print "The force is unbalanced"

