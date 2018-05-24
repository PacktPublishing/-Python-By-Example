'''
Created on Apr 23, 2018
@author: Burkhard A. Meier
'''





import os
import random
import tkinter as tk

CARD_SUITS = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
FACES_ACE = ['Jack', 'Queen', 'King', 'Ace']                # Ace is highest card
NUM_OF_CARDS = 52 

BACK_OF_CARD = 'Back_of_card.gif'
cwd = os.getcwd()
cards_dir = cwd + r'\cards_gif'


class DisplayCardImage():                                   # new class to display one card image
    def __init__(self, card_file):
        win = tk.Tk()
        win.title('Playing cards')
        one_card = tk.PhotoImage(file=os.path.join(cards_dir, card_file))
        width = one_card.width() + 15
        height = one_card.height() + 15
        canvas = tk.Canvas(width=width, height=height, bg='green')
        canvas.pack()
        canvas.create_image(10, 10, anchor='nw', image=one_card)
        win.mainloop()

 
class Card():
    def __init__(self, card_file, file_ext='.gif'):         # pass in file and file ext.
        self.card_file = card_file
        card = card_file.split(file_ext)[0]
        card_rank_suit = card.split('_')
        self.rank = card_rank_suit[0]                       # get rank & suit
        self.suit = card_rank_suit[2]

    def show_card(self, display_image=False):               # optionally show image in GUI
        print('{} of {}'.format(self.rank, self.suit))
        if display_image:
            self.show_card_image()
    
    def show_card_image(self):
        DisplayCardImage(self.card_file)
     
                   

class DeckOfCards():    
    def __init__(self):
        print('creating deck of cards...\n') 
        self.deck_of_cards = os.listdir(cards_dir)
        if BACK_OF_CARD in self.deck_of_cards:                  # remove the 'Back_of_card.gif'
            self.deck_of_cards.remove(BACK_OF_CARD)
        assert len(self.deck_of_cards) == NUM_OF_CARDS, 'Wrong number of cards!'

                   
    def show_deck(self):
        for card in self.deck_of_cards:
            Card(card).show_card()              # cast .gif to Card object
                   
    def shuffle_deck(self):
        print('shuffling deck...\n')
        random.shuffle(self.deck_of_cards)
        
    def draw_card(self):
#         print('drawing a card from the deck...')    
        return self.deck_of_cards.pop()
    
          
class Player():
    def __init__(self, player_name='1'):
        self.player_name = player_name
        self.player_hand = []
        
    def draw_card(self, deck):
#         print('Player *{}* is drawing a card...'.format(self.player_name))
        self.player_hand.append(deck.draw_card())
        return self                                                         # enable chaining of method calls by returning instance of player

    def show_hand(self, display_image=True):
        print('showing cards in hand:')
        for card in self.player_hand:
            Card(card).show_card(display_image=display_image)              # cast .gif to Card object and set bool to True


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
    
    
    
    














































