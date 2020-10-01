print("\t\tPython Program to Calculate Factorial of a Given Number")
print("Created by Rootsec\n")
print('''NOTE:
Type '-1' to stop''')
while 1:
    
    num=int(input("\nEnter non negative number: "))
    fact=1
    if(num==-1):
        break
    for i in range(num):
        fact=fact*(i+1)
    print('Factorial of ',num,':',fact)



