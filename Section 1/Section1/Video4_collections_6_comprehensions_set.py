'''
Created on Mar 31, 2018

@author: Burkhard A. Meier
'''




# list of inventory with different upper and lower case strings
inventory = ['car 1', 'CAR 2', 'tree', 'CAR 1', 'tomato PlAnt', 'bucket', 'BUCKET']
print(inventory)

# list using for loop 
inventory_cap = []
for item in inventory:
    inventory_cap.append(item[:1].upper() + item[1:].lower())
print(inventory_cap)

# cast list to set eliminating duplicates
inventory_cap_set = set(inventory_cap)          
print(inventory_cap_set)


# use set comprehension to do it all at once
inventory_clean = { item[:1].upper() + item[1:].lower() for item in inventory }
print(inventory_clean)






