'''
Created on Mar 29, 2018

@author: Burkhard A. Meier
'''




''' Roll endlessly until a certain number is rolled '''
from random import randint

counter = 1                                             # create integer variable
while True:
    random_number = randint(1, 6)    
    print('Roll:', counter, "value:", random_number)
    if random_number == 1:                              # if random number equals 1
        break                                           # break out of loop 
    counter += 1                                        # increase counter
























