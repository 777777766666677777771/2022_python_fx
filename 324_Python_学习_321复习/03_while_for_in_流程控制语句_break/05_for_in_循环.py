for item in 'python': # 第一次取出来的是P, 将P赋值给item, 将item的只输出
    print(item)

# range() 产生一个整数序列， --》》 也是一个可迭代对象
for i in range(10):
    print(i)

# 如果在循环体中不需要使用到自定义变量， 可将自定义变量写为"__"
for __ in range(5):
    print('人生苦短，我用python')

print('使用for循环，计算1到100之间的偶数和')
sum = 0
for item in range(1, 100):
    if item %2 == 0:
        sum += item

print('1到100之间的偶数和：', sum)