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

bulls_on_parade = Song(["\nThey rally around the family",
						"With pockets full of shells"])

hickory_dickory_doc = Song(["\nHickory dickory doc",
							"The mouse ran up the clock",
							"The clock struck two",
							"He dropped his shoe",
							"And dropped the girl off on the next block"])

mama_mama_cant_you_see_1st = Song(["mama mama can't you see",
								"What the corps has done to me",
								"mama mama can't you see",
								"What the corps has done to me"
								])

# setting a dictionary of the lyrics as mama_mama_cant_you_see_2nd
mama_mama_cant_you_see_2nd = ["Put me in a barbers chair",
								"Then the cut off all my hair",
								"mama mama can't you see",
								"What the corps have done to me"]

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

hickory_dickory_doc.sing_me_a_song()

mama_mama_cant_you_see_1st.sing_me_a_song()


# call the 2nd verse of mama mama can't you see, tell sing me a song to print all lines
Song(mama_mama_cant_you_see_2nd).sing_me_a_song()

# puts do re me as the lyrics, and then executes "." sing_me_a_song()
Song(["Do","Re","Mi"]).sing_me_a_song()


