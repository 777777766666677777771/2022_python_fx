# 注意： 在开发时， 应该把模块中的所有全局变量
# 定义在所有函数上方，就可以保证所有的函数、
# 都能够正常的访问到每一个全局变量
num = 10
# 在定义一个全局变量
tille = "黑马程序员"
# 再定义一个全局变量
name = "小明"

def demo():

    print("%d" % num)
    print("%s" % tille)
    print("%s" % name)

# 在定义一个全局变量
tille = "黑马程序员"

demo()

# 再定义一个全局变量
# name = "小明"
