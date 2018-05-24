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

vehicles = {'cars': cars, 'planes': None, 'trains': None}   # create dict with key-value pairs

plane_1 = {'Model': 'Boing 787'}
plane_2 = {'Model': 'Airbus A350'}
planes = {'plane 1': plane_1, 'plane 2': plane_2}
vehicles['planes'] = planes

train_1 = {'Name': 'Orient Express'}
train_2 = {'Name': 'Santa Fe Express'}
trains = {'train 1': train_1, 'train 2': train_2}
vehicles['trains'] = trains

pprint(vehicles)



