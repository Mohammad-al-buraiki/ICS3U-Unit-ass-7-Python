# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is to claculate the total of 
# items prices plus tax


def calculation(food_item, food_cost):
    # here is the calculation
    total = 0
    for loop_counter in range (len(food_item)):
        item = food_item[loop_counter]
        price = food_cost[loop_counter]
        total += price
    
    print("")
    print("The total is {0} $.".format((total)))
    tax = total * 0.15
    plus_tax = tax + total

    return plus_tax


def main():

    # This function gets input
    food_item = []
    food_cost = []

    # Input
    print("Enter grocery items.\n")
    while True:
        single_food_item = input("Enter food item (when done click 'd'): ")
        if single_food_item != "d":
            food_item.append(single_food_item)
            single_food_item_cost = float(input("Enter the cost of {0}: "
                                          .format(single_food_item)))
            food_cost.append(single_food_item_cost)
        else:
            tax = calculation(food_item, food_cost)
            print("The total with + tax is {0} $.".format(tax))
            break


if __name__ == "__main__":
    main()
