'''
Created on Mar 30, 2018

@author: Burkhard A. Meier
'''





def generator_function():
    print('before yield')
    yield 10                            # yield makes it a generator
    print('before second yield')
    yield 20                            # second yield 


gen = generator_function()              # save generator object in variable

print(next(gen))       
print(next(gen)) 
print(next(gen))            # third call to next() causes StopIteration Exception































