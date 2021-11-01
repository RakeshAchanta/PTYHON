ID=int(input("Enter the Consumer ID:"))
unit=int(input("Enter the Units consumed by the cousumer:"))
print("Coustmer ID:",ID)
print("Units Consumed by Coustmer:",unit)
sub=0.0
if 0<=unit<=199:
    bill=unit*1.20 
elif 200<=unit<400:  #or unit<400
    bill=unit*1.50
elif 400<=unit<600:  #or unit<600
  bill=unit*1.80
else:
    bill=unit*2.0    
print("Electricity Bill of cosnumer with ID:",ID,"is", bill)
if bill>400:
    sub=(bill/15)*100
    total=sub+bill
    print("Subcharge=",sub)
    print("Electricity Bill with Subcharge included is:", total)
else:
     print("Electricity Bill without Subcharge is:", bill)
    
    
    
    
