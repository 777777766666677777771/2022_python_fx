class Person(object):  # Person 继承了object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)

    def ijok(self):
        print(self.name, '我草弄吗')

class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no


class Teacher(Person):
    def __init__(self, name, age, teachofvear):
        super().__init__(name,age)
        self.teachofvear = teachofvear


stu = Student('张三', 20, '2001')
teacher = Teacher('李四', 34, 10)
stu.info()
teacher.info()
