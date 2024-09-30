n = 3  
count = 1  

for i in range(1, n + 1):
    for j in range(1, 2 * i):  
        if count < 10: 
            print(count, end=" ")
            count += 1
    print()
