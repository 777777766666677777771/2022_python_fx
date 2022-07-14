  # 单分支结构
def fenhzi():
    money = 1000 # 余额
    s = int(input('请输入取款金额:')) # 取款金额
    # 判断余额是否充足
    if money >= s:
        money -= s
        print('取款成功，余额为：', money)


# 双分支结构 if else, 二选一执行
# '''从键盘录入一个整数， 编写程序让计算机判断是奇数还是偶数'''
def suangfenzhi():
    num = int(input('请输入一个整数：'))

    # 条件判断
    if num%2 == 0:
        print('是偶数', num)
    else:
        print('是奇数', num)


# 多分支结构， 多选一执行
# 从键盘录入一个整数，成绩
# 90--100 A
# 80--89 B
# 70--79 C
# 60--69 D
# 0--59 E
# 小于0或大于100 Wie非法数据（不是成绩的有限范围）
def duofenzhi():
    num = int(input('请输入你的成绩：'))
    if num >= 90:
        print("A级")
    elif num >= 80 and num <= 89:
        print("B级")
    elif num >= 70 and num <= 79:
        print("C级")
    elif num >= 60 and num <= 69:
        print("D级")
    elif num >= 0 and num <= 59:
        print("E级")
    else:
        print("对不起， 成绩有误， 不在成绩的有效范围")


def qinatao_if():
    """
    会员 >= 200 8折
    会员 >= 100 9折
        不打折
    非会员 >= 200 9.5折
        不打折
    :return:
    """
answer = input('你是会员吗？ y/n ：')
money = float(input('请输入你的购物金额：'))
if answer == 'y': # 是会员
    if money >= 200:
        print('打8折 ，付款金额为：', money * 0.8)
    elif money >= 100:
        print('打9折 ，付款金额为：', money * 0.9)
else: # 非会员
    if money >= 200:
        print('打9.5折 ，付款金额为：', money * 0.95)
    else:
        print('不打折 ，付款金额为：', money)

# fenhzi()
print('-------单分支')
# suangfenzhi()
print('--------双分支结构')
# duofenzhi()
print('---------多分支结构')
qinatao_if()
print('---------if_嵌套使用')