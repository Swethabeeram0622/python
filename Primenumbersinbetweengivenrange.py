# prime numbers in between given range
def prime(n):
    fact = 0
    for i in range(1, n+1):
        if n % i == 0:
            fact += 1
    return fact == 2   # returns True if prime, else False

s = int(input("Enter range: "))
c = 0
print("Prime numbers are:")
for n in range(2, s+1):
    if prime(n):
        print(n, end=" ")
        c += 1
print("\nTotal prime numbers:", c)
