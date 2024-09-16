import math

n = int(input("enter the value of n"))
r = int(input("enter the value of r"))

ncr = math.factorial(n)//(math.factorial(r)*math.factorial(n-r))

print(f"the answer is {ncr}")
