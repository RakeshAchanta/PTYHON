n=int(input())
s=1
while n:
    r=n%10
    s*=r
    n=n//10
print(s)    
