# 集合的创建方式
'''第一种创建方式， 使用{}'''
s = {1,2,3,4,5,5,6,6} # 集合中的元素不允许重复
print(s)

'''第二种创建方式， 使用set()'''

s1 = set(range(6))
print(s1, type(s1))

s2 = set ([1,2,4,5,5,5,6,6])
print(s2, type(s2))

s3 = set((1,2,4,4,5,65)) # 集合中的元素是无序的
print(s3, type(s3))

s4 = set('python')
print(s4)

s5 = set({1,2,3,5,5,6,8,848,4})
print(s5, type  (s5))

# 定义一个空集合
s6 = {} # dict字典类型
print(s6, type(s6))

s7 = set()
print(type(s7))

"""
{1, 2, 3, 4, 5, 6}
{0, 1, 2, 3, 4, 5} <class 'set'>
{1, 2, 4, 5, 6} <class 'set'>
{65, 1, 2, 4, 5} <class 'set'>
{'o', 'y', 'p', 't', 'n', 'h'}
{1, 2, 3, 4, 5, 6, 8, 848} <class 'set'>
{} <class 'dict'>
<class 'set'>
"""
