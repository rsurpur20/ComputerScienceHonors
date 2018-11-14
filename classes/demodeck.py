# import card class from separate file, and random shuffle module
from card import Card
from random import shuffle
import random
# deck class keeps track of a deck of cards
# this can be a full deck of cards, or a player's hand, for example
class Deck:
	# sets up full shuffled deck of cards by default
	# if 0 (or any positive number) is passed, an empty deck will be created
	def __init__(self, full_deck=-1):
		if full_deck == -1:
			suits = ["♠","♥","♣","♦"]
			self.cards = [Card(rank, suit) for rank in range(1, 14) for suit in suits]
			# shuffle by default; remove if you want manual shuffling to occur
			self.shuffle()
		else:
			self.cards = []
	# uses the random module's shuffle method to shuffle cards
	def shuffle(self):
		shuffle(self.cards)

	# deals a single card from the list
	# the default is the first card in the list
	# if a number is passed, the card at that location will be dealt
	# error checking would be nice, to prevent dealing cards at positions that don't exist,
	# or to prevent dealing a card when no cards are left in the hand
	def deal(self, position=-1):
		if position==-1: #error checking?
		# a.pop() removes and returns the item in the list
			return self.cards.pop(0) #removes first item in the list which has been dealt
		else:
			return self.cards.pop(position)

	# add a card to the deck
	def add_card(self, card):
		self.cards.append(card)
		# self.cards=self.cards.sort()
	# def add_randomcard(self,card):
	#         player_deck.add_card(dealer_deck.deal()) #add the card that the dealer deals




	def num_cards(self):
		return len(self.cards)

	# returns the number of cards currently in the deck
	# helper function potentially for deal


	def show_card(self, position=-1):
		if position==-1: #error checking?
		# a.pop() removes and returns the item in the list
			return self.cards[0] #removes first item in the list which has been dealt
		else:
			return self.cards[position]

	# checks to see if a specific card is in the deck
	def contains(self, card):
		for i in self.cards:
			if card.rank == i.rank and card.suit == i.suit:
				return True
		return False

	# for printing out all the cards in the deck in a nice way
	def __str__(self):
		result = ''
		count = 1
		for i in self.cards:
			result += "[card "+str(count)+"] "+str(i)+"\n"
			count=count+1
		return result

	__repr__ = __str__


# remove these when importing deck; for error checking only
dealer_deck = Deck() #full deck
player_deck = Deck(0) #empty deck
removed_cards = Deck(0) #empty deck

# print("DEALER DECK \n")
# print(dealer_deck) #52 cards
for i in range(4): #the range number is the amount of cards that are being dealt to the player
	player_deck.add_card(dealer_deck.deal()) #add the card that the dealer deals
# print(dealer_deck)
print("\nPLAYER DECK")
print(player_deck)
# suits = ["♠","♥","♣","♦"]


# now the user can choose to pick up a random card or pick up a card selected by computer


def computercard():
	# print(dealer_deck()

	player_deck.add_card(dealer_deck.deal()) #add the card that the dealer deals


def randomcard():
	# if they choose a random card
	# if dealer_deck.contains(Card(random.randint(1,14),suits[random.randint(0,3)])):
	#	print("yeet")
	#	# print(dealer_deck(Card(random.randint(1,14),suits[random.randint(0,3)])))
	# print(dealer_deck.show_card(random.randint(0,dealer_deck.num_cards())))

	print("\n***A card has been added to your hand***")
	player_deck.add_card(dealer_deck.deal(random.randint(0,dealer_deck.num_cards()))) #add the card that the dealer deals

	# else:
	#	print("nope")
	# print(dealer_deck.contains(Card(2,"Hearts")))
	# print("PLAYER DECK \n")
	# print(dealer_deck.show_card())

	# print("DEALER DECK \n")
	# print(dealer_deck) #52 cards
# if they choose a card from computer
def userchoice():
	usernum=int(input(("Type 1 to choose the following card:"+str(dealer_deck.show_card())+" Type 2 to choose a random card.\n")))
	# print(dealer_deck.show_card())
	if usernum==1:
		computercard()
		removecard()
	elif usernum==2:
		randomcard()
		removecard()
	else:
		userchoice()
	print("\nYour Hand:")
	print(player_deck)
def removecard_fromuser(cardtoremove):
	removed_cards.add_card(player_deck.deal(cardtoremove-1))
def removecard():
	removed_cards.add_card(dealer_deck.deal())
	# player_deck.remove(dealer_deck.deal())
	# print(removed_cards)
def check_win():

	# first check if all the numbers are the same
	# first sort the numbers
while True:
	userchoice()
	cardtoremove=int(input("What is the number of card you would like to remove?"))
	removecard_fromuser(cardtoremove)
	print("\nYour Hand:")
	print(player_deck)
	check_win()
	# for entry in player_deck:
	#	 hand.append(entry)
	# print(hand)
# if dealer_deck(Card(random.randint(1,14),suits[random.randint(0,3)]))
