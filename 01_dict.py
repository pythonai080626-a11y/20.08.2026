
# int, float
# str
# bool
# list
# None | any
# set
# dict(ionary)
# ['hello','bye'...]  -- key
# [5,      20 ...]    -- value

from pprint import pprint

#  key: value
person = {'first name': 'danny', 'last name': 'cohen', 'age': 20, # str, int, float ...
          'address': {'city': 'Haifa', 'street': 'Eliezer', 'house_number': 7}, # dict
          'kids age': [1, 3, 7],  # list
          'Hobbies': ['Guitar', 'Gym', 'Dancing'],
          'cars': {'Honda', 'Ferrari'},  # set
          frozenset('Gender'): 'F', 'Vegan': True  # bool
          }
# kids = [1, 3, 7]
# for i in range(len(kids)):
#     kids[i] += 1
# print([kid+1 for kid in kids])
print('number of kids=', len(person['kids age']))
print(person)
print('first name=', person['first name'])
print('house number', person['address']['house_number'])
print('city', person['address']['city'])
print('Hobbies', person['Hobbies'][-1])
print('Gender', person[frozenset('Gender')])
# dict: [str, list | dict ]

# An empty dict — {} IS a dict (not a set!)
empty = {}

# Duplicate keys: the LAST one wins
d = {'a': 1, 'a': 2}
print(d)
d['a'] = 3
print(d)

a = dict(name='Dana', age=17)  # → {'name': 'Dana', 'age': 17}
b = dict([ ('x', 1), ('y', 2) ])  # → {'x': 1, 'y': 2}

############################### advanced -- not for now
# From two parallel lists — zip() pairs them up
a   = ['red', 'green', 'blue', 'white']
b = ['#f00', '#0f0', '#00f']
colors = dict(zip(a, b)) # → {'red': '#f00', 'green': '#0f0', 'blue': '#00f'}
print(colors)
##############################################################

animals = ['cat', 'horse', 'ox']
dict_animals = {animal:len(animal) for animal in animals}
print(dict_animals)

# Same starting value for every key
scores = dict.fromkeys(['a', 'b', 'c'], 0)  # → {'a': 0, 'b': 0, 'c': 0}
blank_person = dict.fromkeys(person.keys(), None)
print(blank_person)






















