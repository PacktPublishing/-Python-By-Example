'''
Created on Apr 28, 2018
@author: Burkhard A. Meier
'''




from os import path, getcwd, listdir
from PIL import Image                       # pip install pillow
import tkinter as tk

cwd = getcwd()
cards_dir = cwd + r'\cards_png_large'
cards_dir_smaller = cwd + r'\cards_png_smaller'


def resize_image(image_file, size=(128, 128), ext='_small.png'):
    
    file_name = path.basename(image_file)
    new_image_file = path.splitext(file_name)[0] + ext
    new_image_file_path = path.join(cards_dir_smaller, new_image_file)

    try:
        im = Image.open(image_file)
        im.thumbnail(size)              
        im.save(new_image_file_path)
    except IOError as ex:
        print(ex)
            


class DisplayCardImage():                                   # class to display one card image
    def __init__(self, card_file):
        win = tk.Tk()
        win.title('Playing cards')
        one_card = tk.PhotoImage(file=path.join(cards_dir_smaller, card_file))
        width = one_card.width() + 15
        height = one_card.height() + 15
        canvas = tk.Canvas(width=width, height=height, bg='green')
        canvas.pack()
        canvas.create_image(10, 10, anchor='nw', image=one_card)
        win.mainloop()


all_files = listdir(cards_dir_smaller)
for idx, card_file in enumerate(all_files[:5]):     # display the first 5 card image files
    DisplayCardImage(card_file)




















