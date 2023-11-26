def Palindromic(num):
    num_a =  num[::-1]  
    l = len(num_a)
    for i in range(1,l):
        # 判断是否构成回文
        if (num+num_a[-i:]) == (num+num_a[-i:])[::-1]:
            return num+num_a[-i:]

num = input("please input a num:")
result1 = Palindromic(num)
print(f"回文数1为:{result1}")

