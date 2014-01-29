from sys import argv

#class flash_card(object):
#	def __init__(self, card):
#		self.card = card
#
#	def show_me_a_flash_card(self):
#		for line in self.card:
#			print line

#happy_bday = flash_card(["\nHappy birthday to you",
#					"I don't want to get sued",
#					"So I'll stop right there"])

#bulls_on_parade = flash_card(["\nThey rally around the family",
#						"With pockets full of shells"])

#hickory_dickory_doc = flash_card(["\nHickory dickory doc",
#							"The mouse ran up the clock",
#							"The clock struck two",
#							"He dropped his shoe",
#							"And dropped the girl off on the next block"])#

#mama_mama_cant_you_see_1st = flash_card(["mama mama can't you see",
#								"What the corps has done to me",
#								"mama mama can't you see",
#								"What the corps has done to me"
#								])

## setting a dictionary of the card as mama_mama_cant_you_see_2nd
#mama_mama_cant_you_see_2nd = ["Put me in a barbers chair",
#								"Then the cut off all my hair",
#								"mama mama can't you see",
#								"What the corps have done to me"]

class flash_card(object):
	card = []
	answer = []
	def __init__(self, card, answer):
		self.card = card
#		self.cards.append(card)
		self.answer = answer
#		self.answers.append(answer)

card0 = flash_card('class X(Y)','make a class named X that is-a Y')
card1 = flash_card('class X(object): def __init__(self, J)','class X has-a __init__ that takes self and J parameters.')

print "Question - %s" % flash_card.card
print "Answer - %s" % flash_card.answer

#class Employee(object):
#  locations = []
#  def __init__(self, ldap, name, location, salary, status):
#    self.ldap = ldap
#    self.name = name
#    self.location = location
#    self.locations.append(location)
#    self.salary = salary
#    self.status = status#

#employee1 = Employee('axlr', 'Axl Rose', 'Dublin', 50000, 'active')
#employee2 = Employee('slash', 'Slash', 'Dublin', 50000, 'active')
#employee3 = Employee('peterp', 'Peter Pan', 'New York', 50000, 'active')
#print Employee.locations

# call the 2nd verse of mama mama can't you see, tell sing me a flash_card to print all lines
#for i in range(1, 6):
#	do flash_card(Q1).show_me_a_flash_card() % i 
# print "do flash_card(Q%s).show_me_a_flash_card()" % i
#flash_card(Q1).show_me_a_flash_card()
#raw_input("What does this mean in english? - \nPress Enter to continue...")
#flash_card(A1).show_me_a_flash_card()
#flash_card(Q2).show_me_a_flash_card()
#raw_input("What does this mean in english? - \nPress Enter to continue...")
#flash_card(A2).show_me_a_flash_card()
#flash_card(Q3).show_me_a_flash_card()
#raw_input("What does this mean in english? - \nPress Enter to continue...")
#flash_card(A3).show_me_a_flash_card()
#flash_card(Q4).show_me_a_flash_card()
#raw_input("What does this mean in english? - \nPress Enter to continue...")
#flash_card(A4).show_me_a_flash_card()
#flash_card(Q5).show_me_a_flash_card()
#raw_input("What does this mean in english? - \nPress Enter to continue...")
#flash_card(A5).show_me_a_flash_card()
#flash_card(Q6).show_me_a_flash_card()
#raw_input("What does this mean in english? - \nPress Enter to continue...")
#flash_card(A6).show_me_a_flash_card()#

