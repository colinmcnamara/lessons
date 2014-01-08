name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_centimeters = (height * 2.54)
weight_kilogram = (weight * 0.453592)

print "Let's talk about %s." % name
print "He's %f inches tall." % height
print "He's %f centimeters tall." % height_centimeters
print "He's %f pounds heavy." % weight
print "He's %f kilograms heavy." % weight_kilogram
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %f, %f, and %f I get %f." % (
		age, height, weight, age + height + weight)