n = 4  
count = 1  
for i in range(1, n + 1):
    count = (i * (i + 1)) // 2 
    for j in range(count, count - i, -1):
        print(j, end=" ")
    print()
