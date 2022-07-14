def sum_2_num(num1, num2):
    """读两个数字的求和"""

    result = num1 + num2

    # 可以使用返回值，告诉调用一方函数的返回结果
    return result
    # 注意： retrun 就表示返回， 下方的代码不会被执行到！
    num = 10000

# 可以使用变量，来接受函数返回的结果


sum_result = sum_2_num(52, 1000)

print("计算结果是： %d" % sum_result)

