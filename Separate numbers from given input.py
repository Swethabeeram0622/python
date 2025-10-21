# Separate numbers from given input
def swetha(s):
    b=""
    for i in s:
     if i.isnumeric():
        b+=i
    print(b)
swetha("ists123@gmail.com")
