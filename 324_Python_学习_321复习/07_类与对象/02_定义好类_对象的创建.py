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


# 在类之外定义的函数称为函数， 在类之内定义的称为方法
def drink():
    print('喝水')


# 创建Student类的对象
sut1 = Student('张三', 20)  # 创建对象时的实参 定义在类的初始化方法中
print(type(sut1))
print(id(sut1))
print(sut1)
print('--------------')
print(type(Student))
print(id(Student))  # 类的名称
print(Student)