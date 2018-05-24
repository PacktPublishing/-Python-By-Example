'''
Created on Mar 31, 2018

@author: Burkhard A. Meier
'''





# dictionary with integer data
populations = {'city1': 10000, 'city2': 15000, 'city3': 18000}
print(populations)

# dictionary using loop
total = 0
for value in populations.values():
    total += value
print({'All Cities': total})

# dictionary using list comprehension
total_population = {'All Cities': sum([people for people in populations.values()])}
print(total_population)


# dictionary with list data
populations_two = {'city1 and city2 ': [10000, 15000], 'city3, city4 and city5': [18000, 23000, 35000]}
print(populations_two)

summed_populations = {cities : sum(people) for cities, people in populations_two.items()}
print(summed_populations)



