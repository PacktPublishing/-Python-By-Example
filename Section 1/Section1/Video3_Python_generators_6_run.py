'''
Created on Mar 30, 2018

@author: Burkhard A. Meier
'''



numbers = []                        # create a list
for number_ in range(1, 101):
    numbers.append(number_)          # append 100 numbers to list
# print(numbers)



def generator_multiple_of_three(list_with_numbers):
    print('inside generator')                               # only gets called and printed once                      
    for number in list_with_numbers:                        # generator continuous with next number in list
        if number % 3 == 0:
            yield number                                    # yields number, returning control to calling code


for value in generator_multiple_of_three(numbers):
    if value < 50:                                          # get one value at a time and use it
        print(value, "less than 50")
    else:
        print(value, "greater than 50")




















