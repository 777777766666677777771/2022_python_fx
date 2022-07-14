scores = {'张三': 100, '李四': 98, '王五': 45}
# 获取字典所有的key
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys)) # 将所有的key组成的视图转为列表

# 获取所有的value
values = scores.values()
print(values)
print(type(values))
print(list(values))

# 获取所有的key-value对
items = scores.items()
print(items)
print(list(items)) # 转换之后的列表元素是由元组组成

"""
dict_keys(['张三', '李四', '王五'])
<class 'dict_keys'>
['张三', '李四', '王五']
dict_values([100, 98, 45])
<class 'dict_values'>
[100, 98, 45]
dict_items([('张三', 100), ('李四', 98), ('王五', 45)])
[('张三', 100), ('李四', 98), ('王五', 45)]
"""