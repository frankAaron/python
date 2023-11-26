#螺旋矩阵 4*3
def dfs(arr, x, y, num, l, m, n):
    if l<len(num):
        if n<=0 and m<=0:
            return 0
        if n==1 and m==1:
            arr[x][y] = num[l][0]
            return 0
        # 向右移动
        for i in range(m):
            arr[x][y+i] = num[l][0]
            num[l].pop(0)
        if n-1!=0:
            # 向下
            for i in range(n-1):
                arr[x+1+i][y+m-1] = num[l][0]
                num[l].pop(0)
            # 向左
            for i in range(m-1):
                arr[x+n-1][y+m-2-i] = num[l][0]
                num[l].pop(0)
            if n-2!=0:
                # 向上
                for i in range(n-2):
                    arr[x+n-2-i][y] = num[l][0]
                    num[l].pop(0)
                dfs(arr,x+1,y+1,num,l+1, m-2,n-2)             

#获取不连续数        
def num():
    print("数字之间用逗号（不分中英）隔开")
    n=input("请输入数：")+','
    num=[]
    j=""
    for i in n:       
        if i==','or i=='，':
            num.append(int(j))
            j=""
        else:
            j=j+i
    return num                                   

#获取矩形的长宽
def L_and_W(l):
    x=1
    y=2
    while not x**2<=l<y**2:
        x+=1
        if x**2==l:
            break
        y+=1
    if l>x*y:
        return y,y
    return y,x                               

# 依据大面积减小面积得到一圈的个数    
def mul(x,y):
    if x-2>0 and y-2>0:
        return x*y-(x-2)*(y-2)
    else:
        return x*y                                 

#格式化打印螺旋矩阵(美观)
def pr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j],end="\t")
        print('\n')                                  

print("--------螺旋矩阵--------")
NUM=num()
l=len(NUM)
L,W=L_and_W(l)
while len(NUM)!=L*W:
    NUM.append(' ')

# n = 0
num=[]
# 分组 按圈分组       列表
while L>0 and W>0:
    # 将数按圈移入空列表
    num.append(NUM[:mul(L,W)])
    for i in range(mul(L,W)):
        NUM.pop(0)
    # 每一圈减去两个头和尾
    L-=2
    W-=2
#    n+=1
# 刷新L，W传入dfs
L,W=L_and_W(l)
# 创建二维数组    arr[w][l]
arr = [[0]*L for i in range(W)]                 
dfs(arr, 0, 0, num, 0, L, W)
pr(arr)