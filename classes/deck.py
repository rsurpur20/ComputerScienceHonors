from card import Card
# import random
class Deck:
    def __init__(self):
        decklist=[]
        i=0
        for i in range(1,14):
            # a=str(Card(i, "spades"))
            decklist.append(Card(i, "spades"))
            decklist.append(Card(i, "hearts"))
            decklist.append(Card(i, "diamonds"))
            decklist.append(Card(i, "clubs"))
            i=i+1
    
    def __str__(self):
        # print(decklist)
        return (str(self.rank)+" of "+self.suit)
        # return decklist
        __repr__ = __str__

# print(decklist)
# Deck()
# print()
