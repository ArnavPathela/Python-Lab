n = 5  
for i in range(n, 0, -1):
    print(" " * (n - i) * 2, end="")
    for j in range(1, i+1):
        print(5, end=" ")
    print()
