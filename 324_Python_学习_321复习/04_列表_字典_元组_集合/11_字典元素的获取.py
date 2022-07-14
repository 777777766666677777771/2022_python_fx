'''获取字典的元素'''
scores = {'张三': 100, '李四': 98, '王五': 45}
'''第一种方式 []'''
print(scores['张三'])
# print(scores['柽柳'])

'''第二种方式， 使用get()方法'''
print(scores.get('张三'))
print(scores.get('柽柳')) # None
print(scores.get('麻⑦', 99)) # 99是在查找‘麻⑦’ 所对的value不存在时， 提供的一个默认值
