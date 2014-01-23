people = 30
cars = 40
buses = 15

if cars > people:
	print "We should take cars"
elif cars < people:
	print "We should not take cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's to many buses."
elif buses < cars:
	print "Maybe we should take the buses."
else: print "we still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."
