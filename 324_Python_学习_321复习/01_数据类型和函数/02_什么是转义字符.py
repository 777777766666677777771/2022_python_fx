# 转义字符
# 注意： 转义字符符是使用反斜杠 (\)
print('hello\nworld')   # (\) 加上转义功能的首字母  n-->newline的首字母表示换行
print('hello\tworld')   # (\) 制表符
print('helloooo\tworld')
print('hello\rworld')   # (\) world将hello进行了覆盖
print('hello\bworld')   # (\) \b是退提个格，将o退没了

print('http:\\\\www.baidu.com')
print('你妈说：\‘大家好\’')

# 原字符， 不希望字符串中的转义字符起作用， 就是用原字符， 就是在字符串之前加上r, 或者R
print(r'hello\nworld')
print(r'hello\nworld\\')  # 注意：最后一个字符不能是反斜杠

"""
hello
world
hello	world
helloooo	world
world
hellworld
http:\\www.baidu.com
你妈说：\‘大家好\’
hello\nworld
hello\nworld\\
"""