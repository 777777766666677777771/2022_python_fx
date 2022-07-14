class Student:  # (类名) 可以由一个或多个单词组成， 每个单词首字母大写， 其余小写
    """类的组成
    类属性
    实例方法
    静态方法
    类方法
    """
    native_pace = '广东'  # 直接写在类里的变量， 称为类属性

    # 初始化方法
    def __init__(self, name, age):
        self.name = name  # self.name 称为实体属性， 在这进行了一个赋值操作， 将局部变量的name值赋值给实体属性
        self.age = age

    # 实例方法
    def eat(self):
        print('每天三顿饭...')

    # 静态方法
    @staticmethod
    def method():  # 静态方法 括号内是不用写self的
        print('使用了staticmethod进行修饰， 所以是静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('使用了classmethod进行修饰， 所以是类方法')

# 类属性的使用方式
print(Student.native_pace)
sut1 = Student('张三', 18)
sut2 = Student('李四', 30)
print(sut1.native_pace)
print(sut2.native_pace)
Student.native_pace = '天津'
print(sut1.native_pace)
print(sut2.native_pace)
print('---------类方法的使用方式----------')

# 类方法的使用方式
Student.cm()
print('---------静态方法的使用方式----------')

# 静态方法的使用方式
Student.method()

"""
广东
广东
广东
天津
天津
---------类方法的使用方式----------
使用了classmethod进行修饰， 所以是类方法
---------静态方法的使用方式----------
使用了staticmethod进行修饰， 所以是静态方法

进程已结束,退出代码0
"""