n=int(input())
r=0
k=n
while n:
    x=n%10
    r=r*10+x
    n=n//10  #n value became zero here
if r==k:
    print("Palindrome")
else:
    print("Not a Palindrome")
    
   
   
