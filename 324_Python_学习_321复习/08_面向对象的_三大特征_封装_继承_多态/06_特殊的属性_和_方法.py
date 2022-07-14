"""
# 特殊属性:
__dict__ 获得类对象或实例对象所绑定的所有属性和方法的字典
# 特殊方法：
__len__() 通过重写__1en__()方法，让内置函数1en（)的参数可以是自定义类型
__add__() 通过重写__add__()方法，可使用自定义对象具有'相加'功能
__new__() 用于创建对象
__init__() 对创建对象进行初始化
"""

#print(dir(object))  # dir() 可以查看一个对象有哪些 属性和方法

# 特殊属性
class A:
    pass

class B:
    pass

class C(A,B):
    def __init__(self,name,age):

        self.name = name
        self.age = age

class D(A):
    pass

# 创建一个C类的对象
x = C('jeck',20) # "x" 是 C类的一个实例对象
print(x.__dict__) # __dict__方法，可以查看一个对象的自定义属性 且生成一个字典
print(C.__dict__)
print('------------------------')
print(x.__class__) # __class__ , 输出对象所属的类
print(C.__bases__) # __dases__ , 输出C类，的父类，类型是元组
print(C.__base__) # __dase__ , 输出C类， 的第一个父类 谁在前面就输出谁
print(C.__mro__) # __mro__ , 输出C类 ， 的继承结构
print(A.__subclasses__()) # __subclasses__() 输出A类 , 的所有子类 且生成一个列表

"""
{'name': 'jeck', 'age': 20}
{'__module__': '__main__', '__init__': <function C.__init__ at 0x7fe966d8bdc0>, '__doc__': None}
------------------------
<class '__main__.C'>
(<class '__main__.A'>, <class '__main__.B'>)
<class '__main__.A'>
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
[<class '__main__.C'>, <class '__main__.D'>]
"""


# 特殊方法
print('-----------特殊方法-----------')
print('-----------特殊方法[__add__(), __len__()----------------]')
a = 20
b = 100
c = a + b # 两个整数类型对象的相加操作
d = a.__add__(b)


print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name = name

    def __add__(self,other):
        return self.name+other.name

    def __len__(self):
        return len(self.name)


stu1 = Student("JACK")
stu2 = Student("李四")

s = stu1 + stu2 # 实现了两个对象的加法运算 （因为在Student类中， 编写了__add__（），这个特殊的方法）
print(s)
s = stu1.__add__(stu2)
print(s)
lst = [11,22,33,44]
print(len(lst)) # len是内置函数len
print(lst.__len__())
print(len(stu1))
print('------------特殊方法（__new__()）--------------')
class Person(object):

    def __new__(cls, *args, **kwargs):
        print('__nwe__被调用执行了，cls的Id值为{0}' .format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象的id为{0}'.format(id(obj)))
        return obj

    def __init__(self,name,age):
        print('__init__被调用了，self的id的值为：{0}' .format(id(self)))
        self.name = name
        self.age = age

print('object这个类对象的id为：{0}'.format(id(object)))
print('Person这个类对象的id为:{0}' .format(id(Person)))

p1 = Person('张三', 20)
print('p1这个实例对象的id为:{0}' .format(id(p1)))

"""
object这个类对象的id为：9423968
Person这个类对象的id为:19434992
__nwe__被调用执行了，cls的Id值为19434992
创建的对象的id为140510475981536
__init__被调用了，self的id的值为：140510475981536
p1这个实例对象的id为:140510475981536
"""