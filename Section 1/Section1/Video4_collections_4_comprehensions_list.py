'''
Created on Mar 31, 2018

@author: Burkhard A. Meier
'''




# list with loop
loop_numbers = []                       # create an empty list
for number in range(1, 101):            # use for loop
    loop_numbers.append(number)         # append 100 numbers to list
print(loop_numbers)


# list comprehension
comp_numbers = [ number for number in range(1, 101) ]   # create a new list
print(comp_numbers)


# list comprehension with added condition
comp_numbers_three = [ number for number in range(1, 101) if number % 3 == 0 ]   # multiples of three
print(comp_numbers_three)







