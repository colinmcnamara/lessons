print "You enter a dark room with three doors. Do you go through door #1, #2, #3 or door #4?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. what do you do?"
	print "1. Take the cake"
	print "2. Scream at the bear."
	print "3. Hit the bear with a bat"
	print "4. Grab a giant gun"

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good Job!"
	elif bear == "3":
		print "Are you stupid. That's a bear. He kills you."
	else: 
		print "Well, doing %s is probably better. Bear runs away" % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberrries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
	print "You have stepped into a space ship"
	print "1. Press the red button"
	print "2. Press the blue button"
	print "3. Turn around and go back through the door"

	hatch = raw_input("> ")

	if hatch == "1" or hatch == "2": 
		print "You have released the chritens, you have been eaten"
	else: 
		print "You walked into the cold vacum of space and died"

else:
	print "You stublme around and fall on a knife and die. Good job!"

