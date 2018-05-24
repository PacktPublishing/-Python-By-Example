'''
Created on Mar 29, 2018

@author: Burkhard A. Meier
'''



''' Simple dice rolling example '''
from random import randint                          # from the random module import the randint function

repeat = True                                       # create boolean control variable
while repeat:                                       # endless while loop until repeat no longer is True
    print("You rolled", randint(1, 6))              # random number between 1 and 6 (both inclusive)
    print("Do you want to roll again?")
    rsp = input().lower().strip()                   # read input from console, cast to lower case and remove whitespace
    repeat = ("y" == rsp) or ("yes" == rsp)         # continue loop if "y" or "yes"

print("*** End of Game ***")                        # after the loop

























