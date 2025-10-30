# write a program to sum of the digits in a given number
#METHOD 1
n=int(input())
s=0
while(n!=0):
    r=n%10
    s=s+r
    n=n//10
print("sum:",s)  

 #METHOD 2
n = int(input())
s = str(n)
s1 = 0
for p in range(len(s)):
    s1 = s1+int(s[p])
print("sum:", s1)

