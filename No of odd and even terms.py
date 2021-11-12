n=int(input())
r=0
edc=0
odc=0
while n:
    r=n%10
    if r%2==0:
        edc+=1
    else:
        odc+=1
    n=n//10
print(odc,edc)     
      
