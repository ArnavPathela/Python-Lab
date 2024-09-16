for num in range(1,1001):
    nums = str(num)
    length = len(nums)

    sumd = sum(int(digit) ** length for digit in nums)

    if sumd == num and (num ==1 or num>9):
        
        print(num)
