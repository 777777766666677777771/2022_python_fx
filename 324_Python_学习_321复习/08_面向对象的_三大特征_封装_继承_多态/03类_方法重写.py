class Person(object):  # Person 继承了object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)

    # 静态方法
    @ staticmethod
    def uiiu():
        print('我是静态方法')

    # 类方法
    @ classmethod
    def ooo(cls):
        print('我是类方法')

    def ijok(self):
        print(self.name, '我草弄吗')

class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no
    """从写类容"""
    def info(self):
        super().info() # 调用父类的实例方法
        print('学号',self.stu_no)


class Teacher(Person):
    def __init__(self, name, age, teachofvear):
        super().__init__(name,age)
        self.teachofvear = teachofvear
    """从写类容"""
    def info(self):
        super().info() # 调用父类的实例方法
        print('教龄',self.teachofvear)


stu = Student('张三', 20, '2001')
teacher = Teacher('李四', 34, 10)

stu.info()
print('--------------------')
teacher.info()

print('-------------------')
stu.ooo()
stu.uiiu()

"""
张三 20
学号 2001
--------------------
李四 34
教龄 10
-------------------
我是类方法
我是静态方法
"""