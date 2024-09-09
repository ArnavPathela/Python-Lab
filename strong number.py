n=int(input("enter a number"))
ognum = n
sum = 0
while n>0:
    digit = n%10

    fact=1
    for i in range(1,digit+1):
        fact *=i

    sum +=fact

    n//=10

if sum ==ognum:
    print("it is a strong number")
else:
    print("it is not a strong number")
