# Find unused letters in a string
s = input()
s = s.lower()
r = ' '
for p in range(96,123):
    d = chr(p)
    if d not in s:
        r = r+d
print(r)
