'''
Created on Apr 20, 2018
@author: Burkhard A. Meier
'''




import random

CARD_SUITS = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
FACES_ACE = ['Jack', 'Queen', 'King', 'Ace']                        # Ace is highest card
NUM_OF_CARDS = 52
  
class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def show_card(self):
        print('{} of {}'.format(self.rank, self.suit))
                   
        
class DeckOfCards():    
    def __init__(self):
        print('creating deck of cards...\n') 
        regular_cards = [ Card(rank, suit) for rank in range(2, 11) for suit in CARD_SUITS ]
        face_ace_cards = [ Card(rank, suit) for rank in FACES_ACE for suit in CARD_SUITS ]
        self.deck_of_cards = regular_cards + face_ace_cards
        assert len(self.deck_of_cards) == NUM_OF_CARDS, 'Wrong number of cards!'
                
    def show_deck(self):
        for card in self.deck_of_cards:
            card.show_card()
                   
    def shuffle_deck(self):
        print('shuffling deck...\n')
        random.shuffle(self.deck_of_cards)
        
    def draw_card(self):
        print('drawing a card from the deck...')    
        return self.deck_of_cards.pop()
    
          
class Player():
    def __init__(self, player_name='1'):
        self.player_name = player_name
        self.player_hand = []
        
    def draw_card(self, deck):
        print('Player *{}* is drawing a card...'.format(self.player_name))
        self.player_hand.append(deck.draw_card())
        return self                                                         # enable chaining of method calls by returning instance of player

    def show_hand(self):
        print('showing cards in hand:')
        for card in self.player_hand:
            card.show_card()


if __name__ == '__main__':
    deck = DeckOfCards()
    deck.show_deck()
    deck.shuffle_deck()
    deck.show_deck()
    print()
    player1 = Player('John')
    player1.draw_card(deck).draw_card(deck)
    player1.show_hand()
    print()
    player2 = Player('Tim')
    print(player2)
    ret = player2.draw_card(deck).draw_card(deck)   # because self gets returned, we can chain the calls onto one single line
    print(ret)                                      # ret is the same value as player2
    print(player2 is ret)                           # True
    player2.show_hand()    
    
    print('\nremaining cards:', len(deck.deck_of_cards))
    
    
    
    
    
    
    
    
    

