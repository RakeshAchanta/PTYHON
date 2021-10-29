a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>b and a>c:
    print(a, "is greatest of", b, "and", c)
elif b>a and b>c:
     print(b, "is greatest of", a, "and", c)
elif c>a and c>b:
     print(c, "is greatest of", a, "and", b)  
elif a==b and a>c:
    print(a,"or",b, "is greatest than",c)
elif b==c and b>a:
    print(b,"or",c, "is greatest than",a)
elif c==a and a>b:
    print(c,"or",a, "is greatest than",b)
elif a==b and a<c:
    print(c, "is greatest than",a,"and",b)
elif b==c and b<a:
    print(a, "is greatest than",b,"and",c)
elif c==a and a<b:
    print(b,"is greatest than",c,"and",a)
else:
    print("All values are equal")
    
    
