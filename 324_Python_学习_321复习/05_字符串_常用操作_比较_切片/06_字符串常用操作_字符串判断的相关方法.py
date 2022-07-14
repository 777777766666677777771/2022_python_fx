s = 'hello,python'
print('1',s.isidentifier()) # 判断指定的字符串是不是合法的标识符
print('2','hello'.isidentifier())
print('3','张三_'.isidentifier())
print('4','张三_123'.isidentifier())

print('5','\t'.isspace()) # 判断指定的字符串是否全部由空白字符组成（回车，换行，水平制表符）

print('6','abc'.isalpha()) # 判断指定的字符串是否全部由字母组成
print('7','张三'.isalpha())
print('8','张三1'.isalpha())

print('9','123'.isdecimal()) # 判断指定的字符串是否全部由十进制数字组成
print('10','123四'.isdecimal())

print('11','123'.isnumeric()) # 判断指定的字符串是否全部由数字组成
print('12','123四'.isnumeric())

print('13','abc1'.isalnum()) # 判断指定的字符串是否全部由字母和数字组成
print('14','张三123'.isalnum())
print('15','abc!'.isalnum())

"""
1 False
2 True
3 True
4 True
5 True
6 True
7 True
8 False
9 True
10 False
11 True
12 True
13 True
14 True
15 False
"""