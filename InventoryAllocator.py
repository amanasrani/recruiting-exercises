#InventoryAllocator function, input is order and list of warehouses.

def InventoryAllocator(order,warehouses):

    #Variable 'orderInfo' contains the final allocation of warehouses where items in the order will be shipped from.

    orderInfo = []

    #Iterate through all warehouses checking if there are all or some avaialble items from the order.
    #Note: warehouse are pre-sorted based on cost to shipping address.

    for warehouse in warehouses:

        #Variable 'stock' contains the available inventory of a warehouse.
        #Variable 'allocation' contains the order items that can be shipped from this warehouse.

        stock = warehouse['inventory']
        allocation = {warehouse['name']:{}}

        #We check for every item in order if it is in stock at the warehouse.

        for item in order:
            if item in stock and order[item] != 0 and stock[item] != 0:
                if stock[item] >= order[item]:
                    allocation[warehouse['name']][item] = order[item]
                    order[item] = 0
                else:
                    allocation[warehouse['name']][item] = stock[item]
                    order[item] = order[item] - stock[item]

        #Finally if there are items in the order that can be shipped from the warehouse, we append the warehouse name and the items to the final 'orderInfo'

        if len(allocation[warehouse['name']]) != 0:
                orderInfo.append(allocation)

    #Lastly if the order cannot be fullfilled we return an empty 'orderInfo' as desired.
    
    for item in order:
        if order[item] != 0:
            orderInfo = []
    return orderInfo
