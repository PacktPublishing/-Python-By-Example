'''
Created on Mar 30, 2018

@author: Burkhard A. Meier
'''




def regular_function():
    print('inside regular function')
    return 10
    
regular_function()                      # call the function


def generator_function():
    print('before yield')
    yield 10                            # yield makes it a generator

generator_function()                    # nothing gets printed






































