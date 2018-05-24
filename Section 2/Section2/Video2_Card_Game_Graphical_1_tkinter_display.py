'''
Created on Apr 23, 2018
@author: Burkhard A. Meier
'''






import tkinter as tk
import os
from collections import OrderedDict

win = tk.Tk()
win.title('Playing cards')

cwd = os.getcwd()
cards_dir = cwd + r'\cards_gif'

first_card = os.listdir(cards_dir)[0]                           # load first card to get the size
one_card = tk.PhotoImage(file=os.path.join(cards_dir, first_card))

CARD_SPACING = 10                                            
width = 13 * one_card.width() + (CARD_SPACING * 14)             # 13 cards, 10 spaces in between each card plus 10 on each side 
height = 4 * one_card.height() + (CARD_SPACING * 5)
canvas = tk.Canvas(width=width, height=height, bg='green')
canvas.pack()

canvas.update()                     # call update() otherwise only "1" will be returned
print(canvas.winfo_width())
print(canvas.winfo_height())

FACES_ACE = ['Jack', 'Queen', 'King', 'Ace'] 
def create_ordered_cards():
    '''Create a list of the images in the order we wish.
    The names match the .gif file names.'''
    diamonds = [str(idx) +'_of_diamonds.gif' for idx in range(2, 11)]
    diamonds_face_ace = [face + '_of_diamonds.gif' for face in FACES_ACE]
    diamonds += diamonds_face_ace

    hearts = [str(idx) +'_of_hearts.gif' for idx in range(2, 11)]
    hearts_face_ace = [face + '_of_hearts.gif' for face in FACES_ACE]
    hearts += hearts_face_ace

    spades = [str(idx) +'_of_spades.gif' for idx in range(2, 11)]
    spades_face_ace = [face + '_of_spades.gif' for face in FACES_ACE]
    spades += spades_face_ace
    
    clubs = [str(idx) +'_of_clubs.gif' for idx in range(2, 11)]
    clubs_face_ace = [face + '_of_clubs.gif' for face in FACES_ACE]
    clubs += clubs_face_ace

    return diamonds + hearts + spades + clubs

ordered_cards = create_ordered_cards()
card_images_dict = OrderedDict()                        # remembers order of item insertion

for idx, card_name in enumerate(ordered_cards):
    card = os.path.join(cards_dir, card_name)
    card_images_dict[card_name] = tk.PhotoImage(file=card)

def create_and_display_cards():
    x = CARD_SPACING
    y = CARD_SPACING
    for idx, card in enumerate(card_images_dict):
        if (idx % 13 == 0) and (idx > 0):
            x = CARD_SPACING                             # reset horizontal display line
            y += one_card.height() + CARD_SPACING        # increment vertical display line     
        canvas.create_image(x, y, anchor='nw', image=card_images_dict[card], tags=card)
        x += one_card.width() + CARD_SPACING

back_of_card = 'Back_of_card.gif'
def create_back_of_card():
    back_of_card_img = os.path.join(cards_dir, back_of_card)
    card_images_dict[back_of_card] = tk.PhotoImage(file=back_of_card_img)
        
def place_back_of_card(card_x, card_y):
    canvas.create_image(card_x, card_y, anchor='nw', image=card_images_dict[back_of_card], tags=back_of_card)
    
def get_card_clicked(event):                # callback function
    canvas = event.widget
    x = canvas.canvasx(event.x)             # translate windows x,y to canvas x,y
    y = canvas.canvasy(event.y)
    card = canvas.find_closest(x, y)        # find closest widget to click location
    card_x, card_y = canvas.coords(card)    
    tag = canvas.gettags(card)              # get card tag name  
    if len(tag) > 1:
        if 'current' in tag[1]:
            print('deleting card:', tag[0])
            canvas.delete(card)
            place_back_of_card(card_x, card_y)

canvas.bind('<Button-1>', get_card_clicked)     # on left-button mouse click

create_and_display_cards()
create_back_of_card()
win.mainloop()

