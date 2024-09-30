n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=' ')
    print()
    num += 2
