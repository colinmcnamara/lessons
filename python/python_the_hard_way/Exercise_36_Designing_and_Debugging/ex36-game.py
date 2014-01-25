# Game about the grind of conferences
# must use the following
# . Lists
# .. maybe hold each of the choices in a list. 
#    have each room pull validate against an index choice
#    that is +1  (which one do you want, 1, 2 or 3) 
#    user puts 2, then that is (2 - 1) = 1 for the index 
# . Functions
# .. define a function for each room
# . Modules
# .. import modules such as argv
# . New pieces of python in code
# .. Maybe randomizer to randomize choice presentation?
# .... though that only works if you type in name.. or does it?

from sys import argv

list_name = "empty"
action_name = "empty"
listname = "empty"
user_choice = "empty"

def list_total_choices(func_listname):
#	print "list_total_choices Name in func_Listname is %s" % func_listname
	list_total_choices = len(func_listname)
	print "You have %s choices" % list_total_choices

def print_all_choices_with_number(func_listname):
	print "========================"
#	print "print_all_choices_with_number Name in func_Listname is %s" % func_listname
	for i,n in enumerate(func_listname):
		print "Choice %s You can - %s" % (i,n)

def RepresentesInt(func_s):
	""" helper function to test whether a string is an integer """
	try:
		int(func_s)
		return(True) 
	except ValueError:
		return False

## wip - need to work on the upper / lower bounds
#def input_within_bounds_of_list_item(func_user_choice):
#	try:
#		if len(listname) <= user_choice
#		return(True)
#	except ValueError:
#		return False
#
#	print len(listname)
#	print listname

def input_list_choice(func_listname_action):
	global user_choice
	print "What number is your choice?"
	# enumerate list items, return numbers
	user_input = raw_input("> ")

	# testing to see if everything came through correct
	if RepresentesInt(user_input) == True:
		user_choice = int(user_input)
#		print "your listname is %s long" % len(listname)
		if len(listname) < (user_choice + 1):
#			you_are_fired("That choice was not available.")
			you_are_fired()
	else:
#		you_are_fired("You can't follow directions.")
		you_are_fired()

# wip - dependand on input_within_bounds function
#	if input_within_bounds_of_list_item(user_choice) == True:
#		room_function()
#	else:
#		you_are_fired("You can't follow directions.")

def room_function(func_room_name, func_room_statement, func_list_name, func_action_name):

	""" iterate through all the functions per room """
	global listname
	listname = func_list_name
#	print listname 
	# tell the use what situation they are in
	print func_room_statement
	# print all the choices 
#	create_func_list_names(func_room_name)
	# the two choices below are for debugging only
#	print "Room Function list = %s" % func_list_name
#	print "Room Function action = %s" % func_action_name
#	print "\n"
	list_total_choices(func_list_name)
	print_all_choices_with_number(func_list_name)
	input_list_choice(func_action_name)
#	print "Your Choice from Global Variable is %s" % user_choice
#	print "Choosing index number %s from %s" % (user_choice, func_action_name)
	action_name = func_action_name[user_choice]
#	print "going to %s" % action_name

	func_room_name = []
	func_room_statement = []
	func_listname = []
	func_action_name = []
	action_name() 


def you_are_fired():
	""" successful end choice room """
	print "\nYou have bad judgement. This results in you being fired."
	print "\n"
	exit(0)

def you_got_promoted():
	""" failure end choice room """
	print "\nYour boss and the community acknowledge how awesome you are and promote you."
	print "\n"
	exit(0)

def room_start():
	room_function(*room_conference)
	exit(0)

def room_day_off():
	room_function(*room_day_off)
	exit(0)

def room_delegation():
	room_function(*room_delegation)
	exit(0)

def room_just_go():
	room_function(*room_just_go)
	exit(0)
## used for troubleshooting only
#def print_func_list_names():
#	print func_list_name
#	print func_action_name

# room statement

room_conference_statement = "\nYou realize that you have to be at a conference tomorrow. What do you do? \n"
room_conference_list = ["Call in sick", "Send an Employee", "Rush to get ready"]
room_conference_list_action = [room_day_off, room_delegation, room_just_go]
room_conference = ["room_room_conference", room_conference_statement, room_conference_list, room_conference_list_action]

room_day_off_statement = "\nYou called in Sick, taking the day off. What do you do? \n"
room_day_off_list = ["Go Golfing", "Announce you are not avaible but continue to work", "turn off everything and hide"]
room_day_off_list_action = [you_are_fired, room_delegation, you_are_fired]
room_day_off = ["room_room_day_off", room_day_off_statement, room_day_off_list, room_day_off_list_action]

room_delegation_statement = "\nYou decided to delegate your work. What do you do? \n"
room_delegation_list = ["Send your best guy", "send your worst guy", "send mediocre guy"]
room_delegation_list_action = [you_are_fired, you_are_fired, you_got_promoted]
room_delegation = ["room_delegation", room_delegation_statement, room_delegation_list, room_delegation_list_action]

room_just_go_statement = "\nYou decided are just going. What do you do? "
room_just_go_list = ["Take the first flight out", "Push your flight back an hour", "Push your flight back a day"]
room_just_go_list_action = [you_are_fired, you_are_fired, you_are_fired]
room_just_go = ["room_just_go", room_just_go_statement, room_just_go_list, room_just_go_list_action]

#you_are_fired_statement = "You realize that you have to be at a conference tomorrow. What do you do? \n"

# start the game
room_start() 
