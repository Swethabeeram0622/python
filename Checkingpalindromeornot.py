#  check the number is palindrome or not.
n = int(input())
m = n
s =0
while(n!=0):
    r = n%10
    s = (s*10)+r
    n = n//10
if(s==m):
    print("it's a palindrome")
else:
    print("Not a palindrome")
