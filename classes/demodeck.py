# Roshni Surpur
# November 16,2018
# on my honor, I have neither given nor recieved unauthorized aid
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html Accessed November 16,2018
# I also used the code from the demo in class
# This code is for the card game rummy.

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
			suits = ["♤","♡","♧","♢"]
			self.cards = [Card(rank, suit) for rank in range(1, 14) for suit in suits]
			# shuffle by default; remove if you want manual shuffling to occur
			self.shuffle()
		else:
			self.cards = []

	# uses the random module's shuffle method to shuffle cards
	def shuffle(self):
		shuffle(self.cards)
# sorts card
	def sort(self):
		self.cards.sort(key=lambda x: str(x.rank), reverse=True)
		# print("Cards:",self.__str__())
# sorts card
	def selectionSort(self):
		for fillslot in range(len(self.cards)-1,0,-1):
			positionOfMax=0
			for location in range(1,fillslot+1):
				if int(self.cards[location].rank)>int(self.cards[positionOfMax].rank):
					positionOfMax = location

			temp = self.cards[fillslot]
			self.cards[fillslot] = self.cards[positionOfMax]
			self.cards[positionOfMax] = temp

	# deals a single card from the list
	# the default is the first card in the list
	# if a number is passed, the card at that location will be dealt
	# error checking would be nice, to prevent dealing cards at positions that don't exist,
	# or to prevent dealing a card when no cards are left in the hand
	def deal(self, position=-1):
		# if len(self.cards)==0 or position==len(self.cards):
		# 	return False
		if position==-1 or position>len(self.cards):
		# a.pop() removes and returns the item in the list
			return self.cards.pop(0) #removes first item in the list which has been dealt
		else:
			return self.cards.pop(position)

	# add a card to the deck
	def add_card(self, card):
		self.cards.append(card)

	def num_cards(self):
		return len(self.cards)
	# returns the number of cards currently in the deck
	# helper function potentially for deal
	def show_card(self, position=-1):
		if position==-1: #error checking?
		# a.pop() removes and returns the item in the list
			if len(self.cards)==0:
				return False #checks if there are no more cards
			return self.cards[0] #removes first item in the list which has been dealt
		else:
			return self.cards[position]

	# checks to see if a specific card is in the deck
	def contains(self, card):
		for i in self.cards:
			if card.rank == i.rank and card.suit == i.suit:
				return True
		return False
	def compare_ranks(self,position=-1):
		# checking if all the ranks are equal
		if self.cards[position].rank == self.cards[position+1].rank== self.cards[position+2].rank== self.cards[position+3].rank:

			return True
		else:
			return False


	def compare_rankssuits(self,position=0):
		player_deck.sort()
		if self.cards[position].suit == self.cards[position+1].suit== self.cards[position+2].suit== self.cards[position+3].suit:
	# if all suits are equal and ranks are in ascending and decending order
			if self.cards[position].rank-1 == self.cards[position+1].rank and self.cards[position].rank-2== self.cards[position+2].rank and self.cards[position].rank-3== self.cards[position+3].rank:
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
# checking_deck=Deck(0)

#
for i in range(4): #the range number is the amount of cards that are being dealt to the player
	player_deck.add_card(dealer_deck.deal()) #add the card that the dealer deals



# now the user can choose to pick up a random card or pick up a card selected by computer
# if they choose a card from computer
def computercard():
	player_deck.add_card(dealer_deck.deal()) #add the card that the dealer deals

# if they choose a random card
def randomcard():
	print("\n***A card has been added to your hand***")

	player_deck.add_card(dealer_deck.deal(random.randint(0,dealer_deck.num_cards()))) #add the card that the dealer deals
	player_deck.selectionSort()
# user chooses which of the above options
def userchoice():
	usernum=input(("Type 1 to choose the following card:"+str(dealer_deck.show_card())+" Type 2 to choose a random card.\n"))
	# print(dealer_deck.show_card())
	if usernum=="1":
		computercard()
		removecard()
	elif usernum=="2":
		randomcard()
		removecard()
	else:
		print("I did not understand your answer. Try Again:")
		userchoice()
	print("\nYour Hand:")
	player_deck.selectionSort()
	print(player_deck)

def removecard_fromuser(cardtoremove):
	removed_cards.add_card(player_deck.deal(cardtoremove-1))

def removecard():
	removed_cards.add_card(dealer_deck.deal())


print("\nINSTRUCTIONS: This is the game rummy. The goal of this game is to get a 4-card sequence before you run out of cards.\n There are two types of seuqences:")
print("1: All the ranks are equal. Example: 4♠,4♥,4♣,4♦ or Kings♠,Kings♥,Kings♣,Kings♦ ")
print("2: The suits are the same and the ranks are in ascending or decending order. Example: 5♠,6♠,7♠,8♠  or Kings♦,Queens♦,Jack♦,10♦")
print("Rule: You are only allowed to have 4 cards at a time, so every time a card is added to your hand, you must also remove a card from your hand.\n You have two options to add a card to your hand:\n1. You can take the card the computer gives you. \n2. You can pick up a random card.\nYou may not reuse cards")
player_deck.selectionSort()
print("\nYOUR HAND")
print(player_deck)


while True:
	if dealer_deck==False:
		print("You have run out of cards!")
		break
	userchoice()
	cardtoremove=int(input("What is the number of card you would like to remove?"))
	removecard_fromuser(cardtoremove)
	print("\nYour Hand:")
	player_deck.selectionSort()
	print(player_deck)
	if player_deck.compare_ranks()==True:
		print("You have won!")
		break
	if player_deck.compare_rankssuits()==True:
		print("You have won!")
		break
	if dealer_deck.show_card()==False:
		print("There are no more cards to deal! You have lost")
		break
