'''
upper() 把字符串中所有字符都转为大写
lower() 把字符串中所有字符都转为小写
swapcase() 把字符串中所有大写字母转为小写， 把所有小写字母都转为大写字母
capitalize() 把第一个字符转为大写， 把其余字符转换为小写
title() 把每个单词首字母转为大写， 把每个单词的剩余字符转为小写
'''

s = 'hello,python'
a = s.upper() # 转换大写之后， 会产生一个新的字符串对象
print(a, id(a))
print(s, id(s))
b = s.lower() # 转换之后， 会产生一个新的字符串对象
print(b,id(b))
print(s,id(s))
print(b == s)
print(b is s) # False

s2 = 'hello, Python'
print(s2.swapcase())
print(s2.title())

"""
HELLO,PYTHON 139711213062256
hello,python 139711212657392
hello,python 139711211731824
hello,python 139711212657392
True
False
HELLO, pYTHON
Hello, Python
"""