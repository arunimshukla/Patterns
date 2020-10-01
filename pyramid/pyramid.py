#First outer loop is used to handle number of rows and inner nested loop is used to handle number of columns. 
print("\t\t\tPython Program to Print Half Pyramid")
print("Created by Rootsec\n")
while(1):
    rows= input("Enter number of rows: ") #user input for no. of rows
    rows= int(rows)
    if (rows!=0):
        for i in range(0, rows): #outer loop handles number of rows
            for j in range(0,i+1): #inner loop to handle number of columns
                print("*", end='') #print stars
            print("\r") #ending line after each row
    else:
        break








