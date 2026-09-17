import random

# class Card:
#     def __init__(self, suit:str, rank):
#         self.suit = suit
#         self.rank = rank

#     def __eq__(self, card:Card):
#         if isinstance(card,Card):
#             return ((self.suit == card.suit) and (self.rank == card.rank))
#         else:
#             return False

#     def __lt__(self, card:Card):
#         mapper = {"Jack":11,
#                   "Queen":12,
#                   "King":13,
#                   "Ace":14}

#         self_map = mapper[self.rank] if isinstance(self.rank,str) else self.rank

#         if isinstance(card,Card):
#             card_map = mapper[card.rank] if isinstance(card.rank, str) else card.rank
#             return self_map < card_map
#         else:
#             return False

#     def __str__(self):
#         return f"{self.rank} of {self.suit}"

# class Deck:
#     suits = ["Spades","Hearts","Clubs","Diamonds"]
#     ranks = [i for i in range(1,11)]
#     ranks.extend(["Jack","Queen","King","Ace"])
#     cards = []
#     for suit in suits:
#         for rank in ranks:
#             cards.append(Card(suit, rank))

#     def __init__(self):
#         pass
#     def shuffle(self):
#         random.shuffle(self.cards)

#     def sort_deck(self):
#         self.cards = sorted(self.cards)

# deck = Deck()
# deck.shuffle()
# deck.sort_deck()
# print(deck.cards[0])
# print(deck.cards[-1])