n = int(input("enter a number"))
ognum = n
digit = len(str(n))
power=0

while n>0:
    digit1 = n%10

    power +=digit1**digit
    n//=10

if power == ognum:
    print("it is armstrong")
else:
    print("it is not armstrong")
