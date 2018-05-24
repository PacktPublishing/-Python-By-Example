'''
Created on Mar 31, 2018

@author: Burkhard A. Meier
'''





# ------------ Tuples ------------

number_tuple = (1, 2, 3, 4)                     # tuples use parentheses for creation          
letter_tuple = ('a', 'b', 'c', 'd')
mixed_tuple = (1, 'a', 2, 'b', [88, 99])        # can mix different types

print(number_tuple)
print(letter_tuple)
print(mixed_tuple)

print(type(number_tuple))                       # <class 'tuple'>

try:
    number_tuple[0] = 9                         # tuples are immutable, can't change items once assigned
except Exception as e:
    print('** caught Exception:', e)            # TypeError: 'tuple' object does not support item assignment

try:                                            # try to add item to tuples by creating a new tuple
    new_number_tuple = number_tuple + (5)       # TypeError: can only concatenate tuple (not "int") to tuple
except Exception as e:
    print('** caught Exception:', e)

new_number_tuple = number_tuple + (5,)          # have to add a comma to make it a tuple
print(new_number_tuple)

number_tuple = number_tuple + (5,)              # if we reassign to original tuple value, 
print(number_tuple)                             # it appears as if we are updating it

print(id(number_tuple))                         # but they are two different objects
number_tuple = number_tuple + (6,)
print(id(number_tuple))                         # the variable name is now pointing to a new object


print(number_tuple[:])                          # slice operator - entire tuple
print(number_tuple[1:3])                        # start at element 1, end at 3 (exclusive)
print(number_tuple[3:])                         # start at element 3 until the end (inclusive)

