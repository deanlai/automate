stuff = {'rope': 1, 'dagger': 2, 'snack': 10, 'bow': 1, 'arrow': 36, 'gold coin': 53, 'health potion': 4}

def countTotal(inventory): #
    itemTotal = 0
    for item in inventory.keys():
        itemTotal += inventory[item]
    return itemTotal

def showInventory(inventory):
    print('Inventory:')
    for item, count in inventory.items():
        if count > 1:
            print (str(count) + ' ' + item + 's')
        else:
            print (str(count) + ' ' + item)
    print('\nTotal number of items: ' + str(countTotal(inventory)))

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby', 'dragon scale']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

showInventory(stuff)
addToInventory(stuff, dragonLoot)
showInventory(stuff)
addToInventory(stuff, dragonLoot)
showInventory(stuff)
