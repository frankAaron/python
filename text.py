def count(a):
    if a%2 == 0:
        return a//2-1
    else:
        return (a-1)//2

l = input()
n = int(l[-1])
s=l[l.find('[')+1:l.find(']')].split(',')
sum = 0
a = 0
if s.count('1'):
    b = s.index('1')
    for i in s[b:]:
        if i == '0':
            a += 1
        if i == '1':
            sum += count(a)
            a = 0
    sum += (a+b)//2
else:
    sum = len(l)//2
if sum >= n:
    print("True")
else:
    print("False")