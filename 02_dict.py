
d = {'name': 'Dana', 'age': 17}
print(d['name'])  # → 'Dana'

# .get() never crashes
print(d.get('city', 'unknown'))

stock = {'apple': 5, 'banana': 2, 'cherry': 9}
print(stock.keys())
print(list(stock.keys()))

print(stock.values())  # → dict_values([5, 2, 9])

d = {'name': 'Dana', 'age': 17}
# New key → added

# upsert -- insert + update
d['city'] = 'Haifa'  # if 'city' not exist - create, else: overwrite
d['name'] = 'moshe'  # if 'name' not exist - create, else: overwrite
print(d)

d.update({'age': 19, 'grade': 12})
print(d)

###

items_options = {'sword', 'shield', 'staff', 'mace', 'ring', 'boots'}
item_icons_set = {'⚔️', '🛡️', '🪄', '🔨', '💍', '🥾'}
attributes = {
    'name': None,
    'strength': 15, 'dexterity': 12, 'constitution': 14, 'intelligence': 10, 'wisdom': 13, 'charisma': 8,
    'inventory': []
}
# create character
# 1 get the character name -- input from user
# 2 put the name into the 'name' value (key=name, value=user-input)
# 3 each status is between 3-18 , random values for all attributes
# 4 put 2 random items in the inventory
# *Bonus*: ask user to accept/roll-again (name stays the same)