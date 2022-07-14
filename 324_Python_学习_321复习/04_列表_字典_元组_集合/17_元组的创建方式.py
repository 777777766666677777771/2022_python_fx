'''第一种创建方式 使用（）'''
t = ('python', 'world', 89)
print(t)
print(type(t))

t2 = 'python', 'world', 89 # 省略了小括号
print(t2)
print(type(t2))

t3 = ('python') # 如果元组中只有一个元素， 逗号不能省略（，）
print(t3)
print(type(t3 ))

'''第二种创建方式， 使用tuple()'''
t1 = tuple(('python', 'world', 89))
print(t1)
print(type(t1))

'''空元组的创建方式'''
lst = []
lstl = list()

d = {}
d1 = dict()

# 空元组
t4 = ()
t5 = tuple()

print('空列表', lst, lstl)
print('空字典', d, d1)
print('空元组', t4, t5)

"""('python', 'world', 89)
<class 'tuple'>
('python', 'world', 89)
<class 'tuple'>
python
<class 'str'>
('python', 'world', 89)
<class 'tuple'>
空列表 [] []
空字典 {} {}
空元组 () ()"""