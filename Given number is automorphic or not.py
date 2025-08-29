# write a program to check the given number is automarphic or not.
n =int(input())
l = len(str(n))
sq = n*n
r = sq%(10**(l))
if(n==r):
    print("Automarphic number ")
else:
    print("Not automarphic number")
