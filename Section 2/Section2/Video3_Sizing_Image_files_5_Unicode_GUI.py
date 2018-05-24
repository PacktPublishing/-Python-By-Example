'''
Created on Apr 27, 2018
@author: Burkhard A. Meier
'''





import tkinter as tk
from tkinter import ttk
from Section2.Video3_Sizing_Image_files_4_Unicode_cards import Unicode_playing_cards


win = tk.Tk()
win.title('Playing cards unicode')

row, col = 0, 0  
for idx, value in enumerate(Unicode_playing_cards.values()):
    if idx == 52:
        break
    if (idx % 13 == 0) and (idx > 0):
        row += 1
        col = 0
    ttk.Label(win, text=value[2], font=('', 90), foreground=value[3], 
              background='white').grid(row=row, column=col)
    value[4] = row
    value[5] = col
    col += 1


def on_click_flip_card(event):
#     print(event.x, event.y)
    grid = event.widget
    grid_dict = grid.grid_info()
#     print(grid_dict)
    row, col = grid_dict['row'], grid_dict['column']
    back_card = Unicode_playing_cards['PLAYING CARD BACK']
    ttk.Label(win, text=back_card[2], font=('', 90), foreground=back_card[3], 
              background='white').grid(row=row, column=col)
    
win.bind("<Button-1>", on_click_flip_card)


win.mainloop()





