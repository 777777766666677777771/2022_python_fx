#  python 是动态语言， 在创建对象后， 可以动态绑定属性和方法
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '在吃饭')


stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print('---------为stu1动态的绑定属性-------------')
stu1.gender = '女' # 动态绑定性别
print(stu1.name, stu1.age, stu1.gender)
print(stu2.name, stu2.age)
# print(stu2.name, stu2.age, stu2.gender)

print('--------------------------------')
stu1.eat()
stu2.eat()


def show():
    print('定义在类之外的，称为函数')

stu1.show = show()
stu1.show


"""
---------为stu1动态的绑定属性-------------
张三 20 女
李四 30
--------------------------------
张三在吃饭
李四在吃饭
定义在类之外的，称为函数
定义在类之外的，称为函数
"""