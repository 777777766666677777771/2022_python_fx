gl_num = 10
# 在定义一个全局变量
glz_tille = "黑马程序员"
# 再定义一个全局变量
gl_name = "小明"

def demo():

    # 如果局部变量的名字和全局变量的名字相同
    # pycharm会在局部变量下方显示一个灰色的虚线
    num = 99

    print("%d" % num)
    print("%s" % glz_tille)
    print("%s" % gl_name)

# 在定义一个全局变量
# tille = "黑马程序员"

demo()