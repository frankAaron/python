def mat(m):
    n=[]
    for i in range(m):
            n.append(list(map(int,input().split())))
    return n

def sum(A,B,i,p,j):
    sum=0
    for p in range(p):
        sum=sum+A[i][p]*B[p][j] 
    return sum

def Lg(A,B,n,p,m):
    C=[[0]*m for i in range(n)]
    for i in range(n):
         for j in range(m):
             C[i][j]=sum(A,B,i,p,j)
    return C          

put=lambda n:str(int(n%(1e9+7)))  

n,p,m=map(int,input().split())
A,B=map(mat,(n,p))
C=Lg(A,B,n,p,m)
for i in C:
    print(*list(map(put,i)))