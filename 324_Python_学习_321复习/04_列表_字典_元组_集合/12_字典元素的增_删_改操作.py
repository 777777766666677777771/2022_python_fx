'''key的判断'''
scores = {'张三': 100, '李四': 98, '王五': 45}
print('张三' in scores)
print('张三' not in scores)

'''字典元素的删除'''
del scores['张三'] # 删除指定的key-svlue对
# scores.clear() # 清空字典的元素
print(scores)

'''字典的元素的新增-修改操作'''
scores['陈六']=98 # 新增元素
print(scores)
scores['陈六']=100 # 修改元素
print(scores)

"""
True
False
{'李四': 98, '王五': 45}
{'李四': 98, '王五': 45, '陈六': 98}
{'李四': 98, '王五': 45, '陈六': 100}
"""