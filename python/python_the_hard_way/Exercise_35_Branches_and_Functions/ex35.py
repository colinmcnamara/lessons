from sys import exit

def RepresentesInt(s):
	""" helper function to test whether a string is an integer """
	try:
		int(s)
		return(True) 
	except ValueError:
		return False

def gold_room():
	""" exit of game. if you type in anything other than an integer you die. also 
	evaluates the integer to see if it is greater than or less than 50 """
	print "This room is full of gold. How much do you take?"

	next = raw_input("> ")
## troubleshooting block	
## validate what we entered
#	print next
##print out whether it is an integer or not
#	print RepresentesInt(next)
## end troubleshooting block

#Compare the status. If True set it as an integer
	if RepresentesInt(next) == True:
		how_much = int(next)
	else:
		dead("Man, learn to type a number")
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	""" room before the gold_room. checks if taunt bear is entered twice """
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def cthulhu_room():
	""" loop where if you choose wisely you return to start"""
	print "Here you see the great evil cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	next = raw_input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def colin_room():
	""" loop where if you choose wisely you return to start"""
	print "Here you see the great and nerdy Colin."
	print "He stares at you and your beard grows."
	print "Do you shave, or grow a beard?"

	next = raw_input("> ")

	if "grow" or "beard" in next:
		start()
	elif "shave" in next:
		dead("Men don't shave!")
	else:
		colin_room()

def dead(why):
	""" output that kills the player"""
	print why, "Good job!"
	exit(0)

def start():
	""" Starting room outputs are bear_room or cthulhu_room """
	print "You are in a dark room."
	print "There are doors to your right and left and straight"
	print "Which one do you take?"

	next = raw_input("> ")

	if next == "left":
		bear_room()
	if next == "right":
		cthulhu_room()
	if next == "straight":
		colin_room()
# secret code to bypass and go directly to the gold room		
	if next == "1":
		gold_room()
	else:
		dead("You stumble around the room until you starve.")


start()