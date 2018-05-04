# Exercise 1 at https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/lists/exercises_list_and_dictionaries.html
inventory = {'gold' : 500,'pouch' : ['flint', 'twine', 'gemstone'],'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}
inventory['pocket'] = ['seashell','strange berry','lint']
print(inventory)
# .sort()the items in the list stored under the 'backpack' key
backpack = inventory['backpack']
backpack.sort()
inventory['backpack'] = backpack
print(inventory)
# Then .remove('dagger') from the list of items stored under the 'backpack' key
backpack.remove('dagger')
inventory['backpack'] = backpack
print(inventory)
# Add 50 to the number stored under the 'gold' key
inventory['gold'] += 50
print(inventory)
