# Game Gothons from Planet Percel #25
import unittest
# used into test cases to put random integers into health values
from random import randrange

class Scene(object):

	def enter(self):
		pass

class Engine(object):

	def __init__(self, scene_map):
		pass

	def play(self):
		pass

class Death(Scene):
	""" This is where the player dies and should be funny """
	def enter(self):
		pass

class CentralCorridor(Scene):
	""" Starting point with Gothon already standing there """
	def __init__(self, scene_name):
		# WIP not finished
		self.options = {
		'straight': 'sceneA',
		'left': 'sceneB',
		'right': 'sceneC',
		'back': 'sceneD',
		'taunt': 'taunt_list' # refernce a list or random taunts

}
	def enter(self):
		print "You are walking down the Central_Corridor when you see an Gothon standing at the end "
		print "Do you"
		print "Pull this from a dictionary, run, attack, taunt, "


class LaserWeaponArmory(Scene):
	""" 
	This is where the hero gets a neutron bomb to blow up the ship 
	before getting into the escape pod. It has a keypad he has to 
	guess the number for. 
	"""
	def enter(self):
		pass

class TheBridge(Scene):
	""" Another battle scene with a Gothon where the hero places the bomb """
	def enter(self):
		pass

class EscapePod(Scene):
	""" Where the hero escapes but only after guessing the right escape pod """
	def enter(self):
		pass


class Map(object):
	""" Class containing the functions for moving between scenes """

	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def open_scene(self):
		pass

# not positive I can successfully implement my concept here. But it is worth
# a try. trying to create the actors and items as objects
class Actor(object):
	""" Parent class for antagonist / protagonist """
	def __init__(self,name):
		self.name = name
		self.inventory = {
		'health': '10',
		'xp': '1',
		'raygun': '10',
		'neutron_bomb': '0'
}
	def print_inventory(self):
		print "\n--- %s Inventory ---" % self.name
#		print "health: %s \nxp: %s \nraygun: %s \nbomb: %s" % (self.inventory['health'],self.inventory['xp'],self.inventory['raygun'],self.inventory['neutron_bomb'])
		# Much better way of acocmplishing the same print as above
		for key, value in self.inventory.iteritems():
			print "%s: %s" % (key, value) 

	def effect_target(dictionary_item, target):
		""" Change health based on interfaction with items """
		pass

	def use_item(self, actor, dictionary_item, target):
		""" use an item against a target, only if item >= 0, subtract one """
		print "\n--- Using %s on %s ---" % (dictionary_item, target)

		if self.inventory[dictionary_item] >= 1:
			# read the count of the dictionary_item and subtract 1
			# set that value as the new dictionary item and as integer
			i = int(self.inventory[dictionary_item])
			i -= 1 
			# update item count with new number
			self.inventory[dictionary_item] = (i)
			print "You have %s %s uses remaining" % (self.inventory[dictionary_item], dictionary_item)
			# how the fuck do I pass target as value to the target.Gothon.inventory....)
			print "The %s has %s health remaining" % (target.name, target.inventory['health'])
			# subtract one heath from target
#			print .inventory['health'] 
# wip			print "%s health = %s" % (target, target.inventory['health'])

		else:
			print "You have no uses remaining"


#	def use(self, target):
#		""" use item against your opponent"""
#		pass

#class Antagonist(Actor):
#	""" antagonist alien, openonent of Hero """
#	def __init__(self, name):
#		self.name = name
#	def move(self):
#		""" not sure, but want to get started. """
#		pass

#class Hero(Actor):
#	""" Protagonist Hero, oponent of antagonist alien """
#	def __init__(self, name):
#		self.name = name
#	def move(self):
#		""" not sure, but want to get started. """
#		pass

# Test harness

a_map = Map('Central_Corridor')
a_game = Engine(a_map)
a_game.play()
Gothon = Actor('Gothon')
Luke = Actor('Luke')
# print inventory of both actors
Luke.print_inventory()
Gothon.print_inventory()
# example attack class / function
Luke.use_item('Luke','raygun',Gothon)
Gothon.print_inventory()

#experimenting with pyunit
#class test_inventory_modify(unittest.TestCase):

#	def setup(self):


#	def test_health_modify(self):
#		pass

# validate that the health change function works
class Test_inventory_modify(object):
	def __init__(self,name):
		self.name = name

	def Test_item_modify(self, dictionary_item):
		""" Test that items return proper results when modified """
		TestActor = Actor('TestActor')
		self.dictionary_item = dictionary_item
		# In future tests this will pull from functions in game
		# pull the integer value from the list item
		# sets variable randomizer in the range of 0-10
		

		
		h = TestActor.inventory[dictionary_item]
		i = int(h) + 1
		# set the range of the randomizer to be max the current value + 1
		randomizer = randrange(int(i))
		# takes integer randomizer and makes it a negative int
		randomizer = -randomizer
		y = randomizer
		result = int(i) + y
		print "\n--- %s %s results ---" % (self.dictionary_item, self.name)
 		print "h = %s \ny = %s" % (h,y)
 		print "Result is %s" % result
 		if result == int(i) + y and result >= 0:
 			print "Test Passed"
 			# thinkign 1 = dead. 
 		else:
 			print "Test failed"


# possibly pass a arg flag on runtime where --test=on runs the test suite
Test1 = Test_inventory_modify('Test1')
# Possibly write a for loop that loops through all items. 
Test1.Test_item_modify('health')
Test1.Test_item_modify('xp')


