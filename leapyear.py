print("\t\t\t>>Python Program to Check for Leap Year<<") #program heading
print("Created by Rootsec\n")
while(1):
    year=int(input("Enter year to continue and 0 to stop: "))
    if(year!=0):
        if year%4==0: #leap year condition
            print(year,"is a leap year.\n") 
        else: 
            print(year,"is not a leap year.\n")
    else:
        break
