# So in my Deck class, I have set up 52 cards in a deck, now how do I manipulate them?
# I just want to print my deck
# Now that I have imported the Card deck, what does that mean I could do with it?
from card import Card
import random
suits=["spades","clubs","diamonds","hearts"]
class Deck:
    # do I need all these self.'s?
    def __init__(self):
        self.decklist=[]
        self.i=0
        for i in range(1,14):
            # a=str(Card(i, "spades"))
            self.decklist.append(Card(self.i, "spades"))
            self.decklist.append(Card(self.i, "hearts"))
            self.decklist.append(Card(self.i, "diamonds"))
            self.decklist.append(Card(self.i, "clubs"))
            self.i=self.i+1
            # so now my deck of cards is made right?
        # return decklist
    def takerandomcard(self,rank,suit):
        self.decklist.remove(Card(self.rank, str(self.suit)))
        return decklist

    def __str__(self):
        return (str(self.rank)+" of "+self.suit)
        __repr__ = __str__

# I've tried a variety of methods, how do I simply print my deck?
deck1=Deck()
print(deck1)
# print(deck1.takerandomcard(random.randint(1,14),suits[random.randint(0,4)]))

# print(decklist)
# Deck()
# print()
