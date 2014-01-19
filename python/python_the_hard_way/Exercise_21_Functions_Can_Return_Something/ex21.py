def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight,iq)

# a puzzle for extra credit, type it in anyways.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That become: ", what, "Can you do it by hand?"

team_members = 4
cost_per = 100000
margin = 1000000
team_share = 0.1

individual_share = multiply(team_share, divide(subtract(margin, multiply(cost_per, team_members)), team_members))


print "Individual bonus = ", individual_share, "Can you do it by hand?"