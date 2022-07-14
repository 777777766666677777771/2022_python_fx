def dome1():
    return int(input("请输入整数："))


def dome2():
    return dome1()

# 利用异常的传递性， 在主程序捕获异常
try:
    print(dome2())
except Exception as result:
    print("未知错误 %s " % result)

