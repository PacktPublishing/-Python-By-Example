'''
Created on Apr 28, 2018
@author: Burkhard A. Meier
'''




from os import path, getcwd, listdir
from PIL import Image                       # pip install pillow

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
            
            
for file in listdir(cards_dir):
    file_path = path.join(cards_dir, file)
    resize_image(file_path)




























