num = int(input("enter a number"))
divisors =0

for i in range(1,num):
    if(num%i==0):
        divisors+=i

if(divisors == num):
    print("it is a perfect number")

else:
    print("it is not a perfect number")
        
