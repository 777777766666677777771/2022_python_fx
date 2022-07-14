def fun(a, b=10): # (b) 默认值参数
    print(a, b)

# 函数的调用
fun(100)
fun(20,30)

print('hello', end='\t')
print('world')

'''
100 10
20 30
hello	world
'''