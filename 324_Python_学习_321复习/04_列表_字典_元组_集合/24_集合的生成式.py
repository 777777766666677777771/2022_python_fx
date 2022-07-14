# 列表生成式
lst = [i*i for i in range(10)]
print(lst)

# 集合生成式
s = {i*i for i in range(10)}
print(s)

"""
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
"""