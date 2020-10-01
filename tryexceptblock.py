print("\n\t\tPython Program to Perform Division of Two Numbers")
print("Created by Rootsec\n")
print('''NOTE:)
Type exit() to stop''')
num1 = 0
while num1!=100:
    try:
        num1=eval(input("\nEnter dividend: "))
        num2=eval(input("Enter divisor : "))
        num3= num1/num2
        print("Quotient is: ",num3)
    except:
        print("Sorry!! an error occured :(")
        
                  
