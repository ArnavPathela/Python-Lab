num = int(input("enter number here"))
nums=str(num)
length=len(nums)

sum = 0

for i in range(length):
    sum+=int(nums[i])**(i+1)

if sum == num:
    print("it is a disarium number")
else:
    print("it is not a disarium number")
