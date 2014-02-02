# Game Gothons from Planet Percel #25

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
	def enter(self):
		pass

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

# Test harness

a_map = Map('Central_Corridor')
a_game = Engine(a_map)
a_game.play()
