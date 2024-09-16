num = int(input("enter a number"))

nums = str(num)

sum = sum(int(digit) for digit in nums)

if num%sum==0:
    print("it is a harshad number")
else:
    print("it is not a harshad number")
