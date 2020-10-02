i=0
j= 100

print("Prime numbers between", i, "and", j, "are:")

for num in range(i, j + 1):
   if num > 1:
       for k in range(2, num):
           if (num % k) == 0:
               break
       else:
           print(num)
