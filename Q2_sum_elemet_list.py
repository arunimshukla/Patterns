#Python program to print sum of all items in a list.

def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print("Sum of all elements in the list is:", sum_list([10,20,39]))
