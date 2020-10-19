"""
1. Greedy Algorithm


"""
class food(object):
    def __init__(self, n, v, w):
        self.name = n 
        self.value = v 
        self.weight = w
    
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue()/self.getCost()
    
    def __str__(self):
        return self.name + ": <" + str(self.value)\
                + ", " + str(self.calories) + ">"

def buildMenu(names, values, calories):
""" names, values, calories lists of same length.
    name a list of strings
    values and calories lists of numbers
    return list of Foods
"""
    menu = []
    for i in range(len(values)):
        menu.append(food(names[i], values[i], calories[i]))
    return menu

def greedy(items, maxCost, keyfunction):
""" Assumes items a list, maxCost >= 0,
    keyfunction maps elements of items to numbers
""" 
    itemsCopy = sorted(items, key = keyfunction, reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

def testGreedy(items, constraint, keyfunction):
    taken, val = greedy(items, constraint, keyfunction)
    print("Total value of items taken =", val)
    for item in taken:
        print(' ', item)
