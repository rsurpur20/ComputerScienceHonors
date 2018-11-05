
class Card:
    def __init__(self, rank, suit):
        self.rank=rank
        self.suit=suit
    def __str__(self):
        if self.rank==11:
            self.rank="Jack"
        if self.rank==12:
            self.rank="Queens"
        if self.rank==13:
            self.rank="Kings"
        if self.rank==1:
            self.rank="Ace"
        return (str(self.rank)+" of "+self.suit)
        __repr__ = __str__

# for i in range(1,14):
#     # a=str(Card(i, "spades"))
#     fulldeck.append(Card(i, "spades"))
#         # fulldeck.append(Card(i, "hearts"))
#         # fulldeck.append(Card(i, "diamonds"))
#         # fulldeck.append(Card(i, "clubs"))
#     i=i+1
# print(fulldeck)
