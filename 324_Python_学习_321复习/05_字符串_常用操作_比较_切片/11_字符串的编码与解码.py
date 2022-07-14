s = '天涯共此时'
# 编码
print(s.encode(encoding='GBK')) # 在GBK这种编码格式， 一个中文占两个字节
print(s.encode(encoding='UTF-8')) # 在UTF-8这种编码格式， 一个中文占三个字节

"""
b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1'
b'\xe5\xa4\xa9\xe6\xb6\xaf\xe5\x85\xb1\xe6\xad\xa4\xe6\x97\xb6'
"""

# 解码
# bytes 表示就是一个二进制数据（字节类型的数据）
bytes1 = s.encode(encoding='GBK') # 编码
print(bytes1.decode(encoding='GBK')) # 解码

bytes2 = s.encode(encoding='UTF-8')
print(bytes2.decode(encoding='UTF-8'))

"""
天涯共此时
天涯共此时
"""