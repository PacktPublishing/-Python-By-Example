'''
Created on Mar 30, 2018

@author: Burkhard A. Meier
'''




def regular_function():
    print('inside regular function')
    return 10
    
print(regular_function())               # call and print


def generator_function():
    print('before yield')
    yield 10                            # yield makes it a generator


# print(generator_function())             # <generator object generator_function at >
print(next(generator_function()))       # prints and yields 10


































