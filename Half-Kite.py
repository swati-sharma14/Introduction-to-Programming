n = int(input("Enter the number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        if j == 1:
            print(j, end=' ')
        else:
            print(j, end=' ')
    print()
for i in range(n-1, 0, -1):
    for j in range(1, i+1):
        if j == 1:
            print(j, end=' ')
        else:
            print(j, end=' ')
    print()