def test(num):

    print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))

    # 1> 定义一个字符串变量
    result = "hello"

    print("函数要返回数据的内存地址是 %d" % id(result))

    # 2> 将字符串变量返回, 返回的是数据的引用， 而不是数据本身
    return result