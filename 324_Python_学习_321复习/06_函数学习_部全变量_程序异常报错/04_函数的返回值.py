def fun(num):
    odd = []  # 奇数
    even = []  # 偶数
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even



# 函数的调用
lst = [10, 29, 34, 23, 44, 53, 55]
# fun(lst)
print(fun(lst))

'''([29, 23, 53, 55], [10, 34, 44])'''

'''
函数的返回值
（1）如果函数没有返回值【函数执行后不需要给调用处提供数据】 return可以不用写
（2）函数的返回值，如果是1个，直接返回类型
（3）函数的返回值， 如果是多个， 返回的结果为元组
'''


def fum1():
    print('hello')

fum1()


def fun2():
    return 'hello'

res = fun2()
print(res)


def fun3():
    return 'hello', 'world'
print(fun3())


'''
函数在定义时， 是否需要返回值， 看情况而定
'''

'''
hello
hello
('hello', 'world')
'''