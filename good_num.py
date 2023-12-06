n = int(input())
if n % 2 != 0:
    print(-1)
else:
    a = 1
    while True:
        a *= 2
        if a == n:
            print(n)
            break
        elif a > n:
            a //= 2
            print(a, end=' ')
            n -= a
            a = 1