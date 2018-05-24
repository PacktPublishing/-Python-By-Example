'''
Created on Apr 20, 2018
@author: Burkhard A. Meier
'''





import random
from pprint import pprint

suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']

deck = [ (suit, rank) for suit in suits for rank in range(1, 14) ]      # list comprehension

pprint(deck)

random.shuffle(deck)

pprint(deck)

card = deck.pop()
print('card drawn from top of deck is: ', card)

random_card = deck.pop(random.randint(0, len(deck) -1))
print('random card drawn is: ', random_card)



























