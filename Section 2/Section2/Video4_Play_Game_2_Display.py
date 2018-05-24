'''
Created on Apr 28, 2018
@author: Burkhard A. Meier
'''




import os
import tkinter as tk

cwd = os.getcwd()
cards_dir = cwd + r'\cards_gif'

class DisplayCardImagesGame():                                   
    def __init__(self, player1, player2, num_of_cards=2):
        win = tk.Tk()
        win.title('Playing Cards Game')

        card_file = player1.player_hand[0]             
        one_card = tk.PhotoImage(file=os.path.join(cards_dir, card_file))
        
        CARD_SPACING = 10
        width = num_of_cards * one_card.width() + (CARD_SPACING * (num_of_cards +1))
        height = 2 * one_card.height() + (CARD_SPACING * 3)
        canvas = tk.Canvas(width=width, height=height, bg='green')
        canvas.pack()

        card_img_dict = dict()
        x = CARD_SPACING
        y = CARD_SPACING
        for card in player1.player_hand:
            card_img_dict[card] = tk.PhotoImage(file=os.path.join(cards_dir, card))
            canvas.create_image(x, y, anchor='nw', image=card_img_dict[card])
            x += one_card.width() + CARD_SPACING   
        player1.player_hand = []
        
        x = CARD_SPACING
        y += one_card.height() + CARD_SPACING                
        for card in player2.player_hand:
            card_img_dict[card] = tk.PhotoImage(file=os.path.join(cards_dir, card))
            canvas.create_image(x, y, anchor='nw', image=card_img_dict[card])
            x += one_card.width() + CARD_SPACING   
        player2.player_hand = []
                       
        win.mainloop()



















