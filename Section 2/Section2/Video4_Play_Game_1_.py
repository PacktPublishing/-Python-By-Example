'''
Created on Apr 28, 2018
@author: Burkhard A. Meier
'''





# import modules containing game functionality
from Section2.Video1_Card_Game_Textual_2_oop import CARD_SUITS, FACES_ACE           # DeckOfCards, Player
from Section2.Video2_Card_Game_Graphical_2_tkinter_oop import DeckOfCards, Player
from Section2.Video4_Play_Game_2_Display import DisplayCardImagesGame


class CardGame():
    def __init__(self, name1='John', name2='Tim'):
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.player1_score = 0
        self.player2_score = 0       
        
        self.play_game()
    
    def play_game(self):
        print('playing card game...')
        print(CARD_SUITS, FACES_ACE)

        self.deck = DeckOfCards()
        self.deck.shuffle_deck()
        self.deck.show_deck() 
        
        while self.deck.deck_of_cards:
            print(len(self.deck.deck_of_cards))
            self.draw_cards_and_show()
            
        print('\n\nFinal Score:\n{}: {} -- {}: {}'.format(self.player1.player_name, self.player1_score, 
                                                          self.player2.player_name, self.player2_score))
              
    def draw_cards_and_show(self, cards_each=4):
        try:
            for _card in range(cards_each):
                self.player1.draw_card(self.deck)
                self.player2.draw_card(self.deck)
            
            self.check_score()    
            DisplayCardImagesGame(self.player1, self.player2, num_of_cards=cards_each)

        except Exception as ex:
            print(ex)
    

    def check_score(self):
        ''' Compare only cards belonging to the same suit per each round'''
        print()
        FACES_ACE_dict = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
        
        player1_dict = {'clubs': 0, 'spades': 0, 'hearts': 0, 'diamonds': 0}
        hand1 = [card.split('.')[0] for card in self.player1.player_hand]       # remove .gif
        for card in hand1:
            suit = card.split('_')[2]
            player1_dict[suit] += 1
       
        player2_dict = {'clubs': 0, 'spades': 0, 'hearts': 0, 'diamonds': 0}
        hand2 = [card.split('.')[0] for card in self.player2.player_hand]
        for card in hand2:  
            suit = card.split('_')[2]
            player2_dict[suit] += 1

        print(self.player1.player_name, player1_dict)
        print(self.player2.player_name, player2_dict)

        if player1_dict['clubs'] > 0 and player2_dict['clubs'] > 0:
            print('comparing clubs')
            print(hand1, hand2)
            clubs1 = [club.split('_of_clubs')[0] for club in hand1 if 'clubs' in club]
            clubs2 = [club.split('_of_clubs')[0] for club in hand2 if 'clubs' in club]
            print(clubs1, clubs2)  
            
            clubs1_face_ace = [FACES_ACE_dict[club] for club in clubs1 if club in FACES_ACE_dict.keys()]
            if clubs1_face_ace:
                highest_club1 = max(clubs1_face_ace)
            else:
                highest_club1 = max(int(club) for club in clubs1)      

            clubs2_face_ace = [FACES_ACE_dict[club] for club in clubs2 if club in FACES_ACE_dict.keys()]
            if clubs2_face_ace:
                highest_club2 = max(clubs2_face_ace)
            else:                       
                highest_club2 = max(int(club) for club in clubs2)      
             
            if highest_club1 > highest_club2:
                self.player1_score += 1
            elif highest_club2 > highest_club1:
                self.player2_score += 1
        
                           
        if player1_dict['spades'] > 0 and player2_dict['spades'] > 0:
            print('comparing spades')
            print(hand1, hand2)
            spades1 = [spade.split('_of_spades')[0] for spade in hand1 if 'spades' in spade]
            spades2 = [spade.split('_of_spades')[0] for spade in hand2 if 'spades' in spade]
            print(spades1, spades2)  
            
            spades1_face_ace = [FACES_ACE_dict[spade] for spade in spades1 if spade in FACES_ACE_dict.keys()]
            if spades1_face_ace:
                highest_spade1 = max(spades1_face_ace)
            else:
                highest_spade1 = max(int(spade) for spade in spades1)      

            spades2_face_ace = [FACES_ACE_dict[spade] for spade in spades2 if spade in FACES_ACE_dict.keys()]
            if spades2_face_ace:
                highest_spade2 = max(spades2_face_ace)
            else:                       
                highest_spade2 = max(int(spade) for spade in spades2)      
             
            if highest_spade1 > highest_spade2:
                self.player1_score += 1
            elif highest_spade2 > highest_spade1:
                self.player2_score += 1
        
                            
        if player1_dict['hearts'] > 0 and player2_dict['hearts'] > 0:
            print('comparing hearts')
            print(hand1, hand2)
            hearts1 = [heart.split('_of_hearts')[0] for heart in hand1 if 'hearts' in heart]
            hearts2 = [heart.split('_of_hearts')[0] for heart in hand2 if 'hearts' in heart]
            print(hearts1, hearts2)  
            
            hearts1_face_ace = [FACES_ACE_dict[heart] for heart in hearts1 if heart in FACES_ACE_dict.keys()]
            if hearts1_face_ace:
                highest_heart1 = max(hearts1_face_ace)
            else:
                highest_heart1 = max(int(heart) for heart in hearts1)      

            hearts2_face_ace = [FACES_ACE_dict[heart] for heart in hearts2 if heart in FACES_ACE_dict.keys()]
            if hearts2_face_ace:
                highest_heart2 = max(hearts2_face_ace)
            else:                       
                highest_heart2 = max(int(heart) for heart in hearts2)      
             
            if highest_heart1 > highest_heart2:
                self.player1_score += 1
            elif highest_heart2 > highest_heart1:
                self.player2_score += 1

            
        if player1_dict['diamonds'] > 0 and player2_dict['diamonds'] > 0:
            print('comparing diamonds')
            print(hand1, hand2)
            diamonds1 = [diamond.split('_of_diamonds')[0] for diamond in hand1 if 'diamonds' in diamond]
            diamonds2 = [diamond.split('_of_diamonds')[0] for diamond in hand2 if 'diamonds' in diamond]
            print(diamonds1, diamonds2)  
            
            diamonds1_face_ace = [FACES_ACE_dict[diamond] for diamond in diamonds1 if diamond in FACES_ACE_dict.keys()]
            if diamonds1_face_ace:
                highest_diamond1 = max(diamonds1_face_ace)
            else:
                highest_diamond1 = max(int(diamond) for diamond in diamonds1)      

            diamonds2_face_ace = [FACES_ACE_dict[diamond] for diamond in diamonds2 if diamond in FACES_ACE_dict.keys()]
            if diamonds2_face_ace:
                highest_diamond2 = max(diamonds2_face_ace)
            else:                       
                highest_diamond2 = max(int(diamond) for diamond in diamonds2)      
             
            if highest_diamond1 > highest_diamond2:
                self.player1_score += 1
            elif highest_diamond2 > highest_diamond1:
                self.player2_score += 1
                
            
if __name__ == '__main__':
    game = CardGame()






