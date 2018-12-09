import random
import csv
import operator

productTable = {}
items = []

def populate_products_database():
    with open('uploading/flexdata.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            name = row[2]
            price = float(row[3])
            location = row[0]
            item_type = row[1]
            productTable[name] = (location, item_type)
            newRow = [name, price]
            items.append(newRow)
            
def optimize(flexAmount):
    populate_products_database()
    flexAmount = int(flexAmount*20)
    numItems = len(items)

    dpTable = [[0] * (flexAmount+1) for i in range(numItems+1)]
    parentTable = [[0] * (flexAmount+1) for i in range(numItems+1)]

    for itemSet in range(1, len(dpTable)):
        
        # randomizing the value to come up with different suggestions between 1-5
        itemValue = random.randint(1,6)

        for cost in range(1, len(dpTable[0])):
            loseIt = dpTable[itemSet-1][cost]
            itemPrice = int(items[itemSet-1][1]*20)
            if itemPrice > cost:
                useIt = 0
            else:
                useIt = itemValue + dpTable[itemSet-1][cost-itemPrice]

            if useIt < loseIt:
                parentTable[itemSet][cost] = cost
            else:
                parentTable[itemSet][cost] = cost - itemPrice
            dpTable[itemSet][cost] = max(useIt, loseIt)

    # reconstruct solution
    currentCol = flexAmount
    flexLeft = flexAmount/20
    listOfSuggestions = {}

    for itemSet in range(len(dpTable)-1, -1, -1):
        newCol = parentTable[itemSet][currentCol]
        if not (newCol == currentCol):
            listOfSuggestions[items[itemSet-1][0]] = items[itemSet-1][1]
        currentCol = newCol

    sorted_x = sorted(listOfSuggestions.items(), key=operator.itemgetter(1))
    newList = {}
    for item in listOfSuggestions:
        price = listOfSuggestions[item]
        if flexLeft >= 0:
            newList[item] = price
            flexLeft = flexLeft-price
        else:
            return newList
    return newList
