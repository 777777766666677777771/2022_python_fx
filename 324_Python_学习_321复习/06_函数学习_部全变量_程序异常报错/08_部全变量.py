def fun(a,b):
    c = a+b # 因为c是在函数体内进行定义的变量， a,b 为函数的形参， 作用范围也是函数的内部， c，a,b就相当于局部变量
    print(c)

# print(c) # 局部变量 外部无法使用， 程序报错
# print(a)

name = '全局变量' # name在函数内部外部都可是使用， -->称为全局变量
print(name)
def fun2():
    print(name)
# 调用函数
fun2()

def fun3():
    global age # 函数内部定义的变量， 使用global声明后， 实际上就是全局变量
    age = '局部变量'
    print(age)
fun3()
print(age)

"""
全局变量
全局变量
局部变量
局部变量
"""