n = int(input("Enter the number: "))
if n % 2 == 0:
    for i in range(1, n+1):
        t = (2*i) - 1
        print(' ' * (n-i), end='')
        for j in range(1, t+1):
            print(j, end=' ')
        print()
    for i in range(n-1, 0, -1):
        t = (2*i) - 1
        print(' ' * (n-i), end='')
        for j in range(1, t+1):
            print(j, end=' ')
        print()
