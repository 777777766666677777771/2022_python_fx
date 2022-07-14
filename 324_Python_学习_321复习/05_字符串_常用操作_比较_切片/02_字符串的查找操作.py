'''
index, rindex, find, rfind
'''

s = 'hello,hello' #
print(s.index('lo')) # 3
print(s.find('lo')) # 3
print(s.rindex('lo')) # 9 查找最后出现索引
print(s.rfind('lo')) # 9 查找最后出现索引

# print(s.index('k')) # ValueError: substring not found
print(s.find('k'))
# print(s.rindex('k')) # ValueError: substring not found
print(s.rfind('k'))

'''
3
3
9
9
-1
-1

'''