# write the program to find no.of vowels and consonents in the string.

s = input()
v = "aeiou"
vc = 0
cc = 0
for p in s:
    if p in v:
        vc = vc+1

    elif((p not in v)and(p!= " ")):
        cc = cc+1
print(vc)
print(cc)
