n=int(input("Enter a number of the Month"))
if n==2:
    print("Month", n, "has 28 days")
elif n==4 or n==6 or n==9 or n==11:
    print("Month", n, "has 30 days")
elif n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
    print("Month", n, "has 31 days")
else:
    print("Enter a valid Month number")
    
