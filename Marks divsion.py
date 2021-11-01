rollnum=int(input("Enter he Roll Number:"))
phy=int(input("Enter the Marks in Physics:"))
che=int(input("Enter the Marks in Chemistry:"))
cs=int(input("Enter the Marks in Computer Science:"))
total=phy+che+cs
percent=(total/300)*100
print("Total Marks of Roll no", rollnum, "is", total)
print("Percentage of Student with Roll no", rollnum, "is", percent)
if 80<=percent<=100:
    print("First")
elif 70<=percent<=79:
    print("Second")
elif 60<=percent<=69:
    print("Third")
elif 50<=percent<=59:
    print("Fourth")
elif 0<=percent<=49:
    print("Fail")
else:
    print("Check the input values")
