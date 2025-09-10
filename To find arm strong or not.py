n = input()
sum = 0
total = 0
for i in n:
    total = int(i) **3
    sum += total
if sum == int(n):
    print("arm strong")
else:
    print("Not armstrong")  
