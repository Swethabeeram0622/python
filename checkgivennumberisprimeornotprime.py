# given number is prime or not
s=int(input())
fact=0
for i in range(1,s+1):
    if s%i==0:
        fact +=1
if fact==2:
    print("prime")
else:
    print("not prime")    
