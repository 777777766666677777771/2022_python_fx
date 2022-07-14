# 测试对象的布尔值
print('-------------以上对象的布尔值为False----------------')
print(bool())
print(bool(False)) # False
print(bool(0)) # False
print(bool(0.0)) # False
print(bool(None)) # False
print(bool('')) # False
print(bool("")) # False
print(bool([])) # 空列表
print(bool(list())) # 空列表
print(bool(())) # 空元组
print(bool(tuple())) # 空元组
print(bool({})) # 空字典
print(bool(dict({})))# 空字典
print(bool(set())) # 空集合

"""
-------------以上对象的布尔值为False----------------
False
False
False
False
False
False
False
False
False
False
False
False
False
False
"""

print('-----------------其它对象的布尔值都为True-----------------')
print(bool(18))
print(bool(True))
print(bool('hello, python'))

"""
-----------------其它对象的布尔值都为True-----------------
True
True
True
"""