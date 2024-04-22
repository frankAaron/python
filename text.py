def now():
    print("2024")
f = now
f()
class student:
    def __init__(self,name,age): 
        #私有
        self.__name = name
        self.__age = age
    #获取并修改属性
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.name = name or '无名氏'

    def good_stu(self,class_name):
        print(f"正在学习{class_name}")
stu1 = student('python',20)      
print(stu1.good)