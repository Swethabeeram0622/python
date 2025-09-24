# write a program to check the given strings are anagram or not.
s1 = input()
s2 = input()
s = sorted(s1) #["a", "e", "t"]
r = sorted(s2) #["a", "e", "t"]
if(s==r):
    print("Anagram")
else:
    print("Not an anagram")
