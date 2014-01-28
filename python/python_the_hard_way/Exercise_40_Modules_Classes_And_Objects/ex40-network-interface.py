from sys import argv

class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["\nHappy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])


# call the 2nd verse of mama mama can't you see, tell sing me a song to print all lines
Song(mama_mama_cant_you_see_2nd).sing_me_a_song()

# puts do re me as the lyrics, and then executes "." sing_me_a_song()
Song(["Do","Re","Mi"]).sing_me_a_song()


