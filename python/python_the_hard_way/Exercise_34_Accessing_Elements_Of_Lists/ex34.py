# using radomizer for test
from random import choice

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
years = ['2000', '2001', '2002', '2003', '2004', '2005','2006', '2007', '2008', '2009', '2010',   ]

def list_enumerate_answers(item_name, listname):
	for index, list_item in enumerate(listname):
		print "The %s at index num %s is %s " % (item_name, index, list_item)

def list_enumerate(listname):
	for index, list_item in enumerate(listname):
		print "The  index num ? is %s " % (list_item)

# using python to check answers
# if user inputs the correct index number for the list then execute the rest of the code
print "\nTime for a test on lists"
print "Here is the list of animals\n"
list_enumerate(animals)
print ""

#answer = raw_input()
#maybe pick at random from the list?

item = choice(animals)
indexnumber = animals.index(item)

print "What is the index number for %s in the list we just printed" % item
# raw input comes as a string. we need to make sure this is a number...
answer = int(raw_input("> "))
# used for troubleshooting the fact that I was not capturing the raw_input as
# and integer
# print "Your answer was %s and the indexnumber was %s " % (answer, indexnumber) 

if answer == indexnumber:
	print "You Rock! The answer %s was index number %s " % (item, indexnumber)
elif answer < indexnumber:
	print "You Suck! The answer %s was less than indexnumber %s " % (item, indexnumber)
elif answer > indexnumber:
	print "You Suck! The answer %s was greater than indexnumber %s " % (item, indexnumber)
else:
	print " Meh"
# make the answer visible to the screen before continuing 
raw_input("Press Enter to continue...")

# for loop for mental exercize 
listnum = 0
print "\nUsing a for loop to enumerate"
for i in range (1, 7):
	print "the animal in number %s place in the list is index %s %s " % (i, listnum, (animals[listnum]))
	listnum += 1

# note, had to put quotes around animals. When there are not quote
# python was looking for a variable instead of passing that string
# to the called function
print "\nUsing a function with a for loop to enumerate Animals"
list_enumerate_answers("animal", animals)

print "\nUsing a function with a for loop to enumerate Years"
list_enumerate_answers("year", years)






