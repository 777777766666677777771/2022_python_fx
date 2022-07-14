s = 'hello,python'
s1 = s[:5] # 由于没有指定起始位置， 所以从0开始切
s2 = s[6:] # 由于没有指定结束位置， 所以切到字符串的最后一个元素
s3 = '!'
newstr = s1 + s3 + s2

print(s1)
print(s2)
print(newstr)

print('---------------')
print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))

print('--------切片[start:end:step]-------')
print(s[1:5:1]) # 从1开始切到5（不包含5）， 步长为1
print(s[::2]) # 默认从0开始， 没有写结束， 默认到字符串的最后一个元素。步长为2， 两个元素之间的索引间隔为2
print(s[::-1]) # 默认从字符串的最后一个元素开始， 到字符串的第一个与元素结束，因为步长为负数
print(s[-6::1]) # 从索引-6开始， 到字符串的最后一个元素结束， 步长为1

"""
hello
python
hello!python
---------------
140311519074032
140311517784880
140311517784944
140311518709552
--------切片[start:end:step]-------
ello
hlopto
nohtyp,olleh
python
"""