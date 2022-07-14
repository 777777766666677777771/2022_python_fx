# else 与 for 搭配
def else_for():
    for item in range(3):
        pwd = input('请输入密码:')
        if pwd == '888':
            print('密码正确')
            break
        else:
            print('密码不正确')
    else:
        print('对不起三次密码均输入错误')

# else 与 while 搭配
def else_while():
    a = 0
    while a <3:
        pwd_1 = input('请输入密码：')
        if pwd_1 == '8888':
            print('密码正确')
            break
        else:
            print('密码不正确')
            # 改变a变量
    else:
        print('对不起三次密码均输入错误')


# else_for()
else_while()
