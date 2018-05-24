'''
Created on Mar 31, 2018

@author: Burkhard A. Meier
'''





# ------------ Lists ------------

number_list = [1, 2, 3, 4]                      # lists use square brackets for creation          
letter_list = ['a', 'b', 'c', 'd']
mixed_list = [1, 'a', 2, [1, 2, 3, 4]]          # can also nest lists within lists

print(number_list)
print(letter_list)
print(mixed_list)

print(type(number_list))                        # <class 'list'>

original_value = number_list[0]                 # save value at index 0
number_list[0] = 9                              # lists are mutable, can change items once assigned
print(number_list)
number_list[0] = original_value                 # reassign original value
print(number_list)

number_list.append(5)                           # add item to list via append
print(number_list)

number_list += [6]                              # add item to list via operator
print(number_list)

new_number_list = number_list[:]                # copy entire list via slicing
print(new_number_list)
print(id(number_list))                          # different ids 
print(id(new_number_list))
print()

other_number_list = number_list                 # create second reference to same list object
print(id(number_list))                          # same ids
print(id(other_number_list))                    # pointing to the same object

number_list.append(99)                          # append to first list
print(other_number_list)                        # second list also shows the new value

print(number_list[:])                           # slice operator - entire list
print(number_list[1:3])                         # start at element 1, end at 3 (exclusive)
print(number_list[3:])                          # start at element 3 until the end (inclusive)

