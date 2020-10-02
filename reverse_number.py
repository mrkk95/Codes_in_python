def Reverse(Number):  # Function Definition
  rev = 0
  while(Number > 0):
    rem = Number %10
    rev = (rev *10) + rem
    Number = Number //10
  return rev

Number = int(input())
rev = Reverse(Number)  # Function Call
print("%d" %rev)
