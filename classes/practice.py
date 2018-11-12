# card class represents a single card in a deck
import random
class Card:

	# card class keeps track of rank and suit for a single card
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	# print out the rank and suit in a nice way for the card
	# rank is stored as a number, but will display as a word here
	def __str__(self):
		rank = self.rank
		if self.rank == 11:
			rank = "Jack"
		elif self.rank == 12:
			rank = "Queen"
		elif self.rank == 13:
			rank = "King"
		elif self.rank == 1:
			rank = "Ace"
		return str(rank)+" of "+self.suit

	__repr__ = __str__

symbol=["Hearts","Spades","Clover","Diamonds"]
# remove these when card class is imported; for error checking only
card1 = Card(random.randint(1,14), symbol[random.randint(0,3)])
print(card1)
