phy=int(input("Enter marks in Physics:"))
che=int(input("Enter marks in Chemistry:"))
mat=int(input("Enter marks in Mathematics:"))
eng=int(input("Enter marks in English:"))
lit=int(input("Enter marks in Literature:"))
tot=phy+che+mat+eng+lit
percent=(tot/500)*100
print("TOTAl MARKS OF THE STUDENT IS:",tot)
print("PERCENTAGE OF THE STUDENT IS:", percent)
