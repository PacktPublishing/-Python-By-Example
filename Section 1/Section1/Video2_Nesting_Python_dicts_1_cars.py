'''
Created on Mar 30, 2018

@author: Burkhard A. Meier
'''



cars = {}                   # dictionary for holding cars
print(cars)
print(type(cars))           # type is dictionary
print()

car_1 = {'make': 'BMW', 'speed': 'fast'}            # dict car_1
car_2 = {'make': 'Mercedes', 'speed': 'good'}
car_3 = {'make': 'Porsche', 'speed': 'very fast'}

cars['car 1'] = car_1         # assign car_1 dict to cars, creating new key
cars['car 2'] = car_2
cars['car 3'] = car_3

print(cars)
print()

from pprint import pprint
pprint(cars)
print()

print(cars['car 2']['make'])     # what make is car 2?
print(cars['car 3']['speed'])    # what is the speed of car 3?










