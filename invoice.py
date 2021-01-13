# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is to find the largest number


def calculation(food_item, food_cost):
    # here is the calculation
    total = 0
    for loop_counter in range(0, len(food_item)):
        item = food_item[loop_counter]
        price = food_cost[loop_counter]
        print("{0} = {1} $".format(item, price))
        total += price

    print("the total is {0} $.".format((total)))
    plus_tax = total * 0.15
    print("the total plus tax is {0} $.".format(plus_tax))
    return


def main():

    # This function gets input
    food_item = []
    food_cost = []
    times = 0

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
            break


if __name__ == "__main__":
    main()
