'''
Created on Apr 28, 2018
@author: Burkhard A. Meier
'''




from os import path, getcwd, listdir
from PIL import Image                       # pip install pillow

cwd = getcwd()
cards_dir = cwd + r'\cards_png_large'
cards_dir_smaller = cwd + r'\cards_png_smaller'

first_file = listdir(cards_dir)[0]                  # get first file in dir
first_file_path = path.join(cards_dir, first_file)

im = Image.open(first_file_path)            # use Pillow to open the file
print(im.size)                              # print image file size


def resize_image(image_file, size=(128, 128), ext='_small.png'):
    
    file_name = path.basename(image_file)
    new_image_file = path.splitext(file_name)[0] + ext
    new_image_file_path = path.join(cards_dir_smaller, new_image_file)

    try:
        im = Image.open(image_file)
        im.thumbnail(size)                  # thumbnail keeps aspect ratio
        im.save(new_image_file_path)
        print(im.size)
    except IOError as ex:
        print(ex)
            
                    
resize_image(first_file_path)       # resize first image in dir




























