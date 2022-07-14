def demol():

    # 定义一个局部变量
    # 1> 出生： 执行了下方的代码之后， 才会被创建
    # 2> 死亡： 函数执行完成之后
    num = 10

    print("在demol函数内部的变量是 %d " % num)


def demol2():

    num = 99

    print("demo2 ==> %d" % num)
    pass

# 在函数内部定义的变量，不能再其他位置使用
# print("%d" % num)

demol()
demol2()