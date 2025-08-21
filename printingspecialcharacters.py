# to print special characters only from input.
 def swetha(s):
     b=""
     for i in s:
      if i.isalnum():
         b+=i
     print(b)
 swetha("ists123@gmail.com")
