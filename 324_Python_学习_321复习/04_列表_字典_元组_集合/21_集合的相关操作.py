'''集合元素的判断操作 -- 判断在不在 某个数据集合当中'''
s = {10,20,30,40,50}
print(10 in s) # True
print(100 in s) # False
print(10 not in s) # False
print(100 not in s) # True

'''集合元素的新增操作'''
s.add(80) # add一次添加一个元素
print(s)
s.update({200,400,300}) # 一次至少添加一个元素
print(s)
s.update([100,5543,464])
s.update((10545,46464,46376846))
print(s)

'''集合元素的删除操作'''
s.remove(100) # 一次删除一个指定元素， 指定元素不存在-程序会报错
# s.remove(500) # KeyError: 500
print(s)
s.discard(300) # 一次删除一个指定元素， 指定元素不存在-程序不会报错
print(s)
s.pop() # 一次删除一个任意元素 不能指定删除元素-否者会报错
s.pop()
s.pop()
# s.pop(400) # TypeError: set.pop() takes no arguments (1 given)
print(s)
s.clear()
print(s)