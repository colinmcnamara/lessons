def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def mulitply(a,b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = mulitply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight,iq)

# a puzzle for extra credit, type it in anyways.
print "Here is a puzzle."

what = add(age, subtract(height, mulitply(weight, divide(iq, 2))))

print "That become: ", what, "Can you do it by hand?"
