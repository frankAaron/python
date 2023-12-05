def fection(flowers,n,count):
    l = len(flowers)
    if flowers[0] == 1:
        for i in range(1,l-1):
            if flowers[i-1] == flowers[i+1] == 0 and flowers[i] != 1:
                flowers[i] = 1
                count += 1
        if flowers[-1] == 0 and flowers[-2] == 0:
                count += 1
    elif flowers[0] == 0:
        flowers[0] = 1
        count += 1
        n = n
        return fection(flowers,n,count) 
    if count >= n:
            return 1
    else:
        return 0 
"""l=input()
n=int(l[l.find('n')+2:])
flowers=l[l.find('[')+1:l.find(']')].split(',')"""       
flowers = list(map(int,input().split(" ")))
print("flowers = ",end="")
print(flowers)
print("n = ",end="")
n = int(input())
count = 0
if fection(flowers,n,count):
    print("True")
else:
    print("False")