'''
Created on Mar 29, 2018

@author: Burkhard A. Meier
'''




''' Roll 100 times, gathering statistics
    using a dictionary data structure.'''
from random import randint   
 
dice_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}      # initialize dictionary to zeros
total_score = 0
 
for roll in range(100):                         # roll 100 times inside for loop
    number_rolled = randint(1, 6)           
    dice_dict[number_rolled] += 1               # update dictionary for number rolled
    total_score += number_rolled                # increase total score

     
print('\nTotals:' + '\n' + '=' * 7)        
print(dice_dict)    
 
print('\nTotal Score:' + '\n' + '=' * 12)  
print(total_score)  































