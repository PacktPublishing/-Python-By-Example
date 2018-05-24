'''
Created on Mar 30, 2018

@author: Burkhard A. Meier
'''




from pprint import pprint

cars = {}                   

car_1 = {'make': 'BMW', 'speed': 'fast'}            
car_2 = {'make': 'Mercedes', 'speed': 'good'}
car_3 = {'make': 'Porsche', 'speed': 'very fast'}

cars['car 1'] = car_1         
cars['car 2'] = car_2
cars['car 3'] = car_3


# 3 levels of nesting
vehicles = {'cars': cars, 'planes': None, 'trains': None}   # create dict with key-value pairs

pprint(vehicles)

print()
print(vehicles['cars'])             # access nested dict via its key
print(vehicles['planes'])
print(vehicles['trains'])

print()
vehicles_cars = vehicles['cars']    # assign nested dict to new variable
pprint(vehicles_cars)

print()
print(type(vehicles_cars))          # variable type is dictionary



