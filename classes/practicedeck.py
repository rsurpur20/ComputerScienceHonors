# import card class from separate file, and random shuffle module
from practice import Card
from random import shuffle
# deck class keeps track of a deck of cards
# this can be a full deck of cards, or a player's hand, for example
class Deck:

	# sets up full shuffled deck of cards by default
	# if 0 (or any positive number) is passed, an empty deck will be created
	def __init__(self, full_deck=-1):
		if full_deck == -1:
			suits = ["Spades","Hearts","Clubs","Diamonds"]
			self.cards = [Card(rank, suit) for rank in range(1, 14) for suit in suits]
			# shuffle by default; remove if you want manual shuffling to occur
			self.shuffle()
		else:
			self.cards = []

	# uses the random module's shuffle method to shuffle cards
	def shuffle(self):
		shuffle(self.cards)
    # for printing out all the cards in the deck in a nice way
	def __str__(self):
		result = ''
		for i in self.cards:
			result += str(i)+"\n"
		return result

	__repr__ = __str__
print()
