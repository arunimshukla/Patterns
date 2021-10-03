#Python program to print even numbers in a list

List1 = [1,23,32,87,29,88,43,99,5] #creating a list

for num in List1: #iterating numbers in a list
    if num %2 == 0: #condition checking
        print(num, end = " ")
