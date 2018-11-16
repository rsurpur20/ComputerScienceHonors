# So this class lets me munipulate a single card
class Card:
    def __init__(self, rank, suit):
        self.rank=rank
        self.suit=suit
    def __str__(self):
        temp = str(self.rank)
        if self.rank==11:
            temp="Jack"
        if self.rank==12:
            temp = "Queens"
        if self.rank==13:
            temp = "Kings"
        if self.rank==1:
            temp = "Ace"
        return (temp+self.suit)
    __repr__ = __str__

# for i in range(1,14):
#     # a=str(Card(i, "spades"))
#     fulldeck.append(Card(i, "spades"))
#         # fulldeck.append(Card(i, "hearts"))
#         # fulldeck.append(Card(i, "diamonds"))
#         # fulldeck.append(Card(i, "clubs"))
#     i=i+1
# print(fulldeck)
