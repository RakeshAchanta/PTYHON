age=int(input("Enter the age of a person:"))
if age>0 and age<=12:
    print("The person is a child")
elif age>=13 and age<20:
    print("The person is a teen")
elif age>=20 and age<50:
    print("The person is an adult")
elif age>=50 and age<=100:
    print("The person is of Oldage")
elif age>100:
    print("The person is dead")
else:
    print("Enter a valid age")
