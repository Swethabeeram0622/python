# Swapping 'l' and 'p' in a string
s = input()
s = list(s)
for p in range(len(s)):
    if(s[p]=='l'):
        s[p]='p'
    elif(s[p]=='p'):
        s[p] = 'l'
print(' '.join(s))
