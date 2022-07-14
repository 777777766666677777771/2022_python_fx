def sum_numder(num):

    print(num)
    # 递归的出口， 当参数满足某个条件时， 不在执行函数
    if num == 1:
        return

    # 自己调用自己
    sum_numder(num - 1)


sum_numder(3)