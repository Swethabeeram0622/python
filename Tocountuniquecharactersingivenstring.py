# to count unique characters in given string
s= input()
cnt=0
res=""
for i in s:
    if s.count(i)==1:
        cnt += 1
        res += i
print(cnt,res)  
