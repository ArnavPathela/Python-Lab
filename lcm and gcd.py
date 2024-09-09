a = int(input("enter a number"))
b = int(input("enter a number"))

oga = a
ogb = b

while b:
    a,b = b , a%b
gcd = a


lcm  = abs(oga*ogb)//gcd

print("gcd",gcd)
print("lcm",lcm)
