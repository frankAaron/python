l = map(int,input().split())
n = int(input())
count = 0
for i in l:
    if (n + 30) >= i:
        count += 1
print(count)