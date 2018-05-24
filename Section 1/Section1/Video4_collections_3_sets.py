'''
Created on Mar 31, 2018

@author: Burkhard A. Meier
'''





# ------------ Sets ------------

number_set = {1, 2, 3, 4}                       # sets use curly braces for creation          
letter_set = {'a', 'b', 'c', 'd'}
mixed_set = {1, 'a', 2, (1, 2, 3)}              # types must be "hashable", i.e. immutable
empty_set = set()                               # have to use the set() function, cannot use = {}

print(number_set)
print(letter_set)
print(mixed_set)
print(empty_set)                                # returns: set(). {} would be a dict, not a set

print(type(number_set))                         # <class 'set'>

number_set_unique = {1, 2, 3, 4, 2, 3, 4}       # sets only store unique values  
print(number_set_unique)                        # {1, 2, 3, 4}, ignores dupes

number_set.add(5)                               # add an item to the set
print(number_set)

number_set.add(4)                               # try to add existing item to the set
number_set.add(5)                               # try to add existing item to the set
print(number_set)                               # no duplicates, nothing got added

number_set.remove(1)                            # remove an item from the set
print(number_set)

try:                                            # if the item is not in the set
    number_set.remove(98)                       # KeyError: 98 
except Exception as e:
    print('** caught Exception:', e) 

                                                # use the 'in' keyword
print(98 in number_set)                         # False
print(5 in number_set)                          # True















