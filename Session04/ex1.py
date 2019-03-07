inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

value = ['seashell','strange','berry','lint']
inventory['pocket'] = value

inventory['backpack'].remove('dagger')

inventory['gold'] += 50
print(inventory)