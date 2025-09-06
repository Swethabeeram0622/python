# write a program to check the string is palindrome or not.
s = input()
p1 = 0
p2 = len(s)-1
f = 1
while(p1<p2):
    if(s[p1]!=s[p2]):
        f = 0
        break
    p1 = p1+1
    p2 = p2-1
if(f==1):
    print("palindrome")
else:
    print("not a palindrome")
