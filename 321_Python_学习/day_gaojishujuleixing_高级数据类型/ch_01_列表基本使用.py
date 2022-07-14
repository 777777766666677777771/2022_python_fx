name_lit = ["zhangsan", "lisi", "wangwu"]
# 1.取值和取索引
# list index out of range - 列表索引超出范围

print(name_lit[1])

# 知道数据的类容， 想确定数据在列表中的位置
# 使用index方法需要注意，如果传递的数据不在列表中，程序会报错！
print(name_lit.index("wangwu"))

# 2.修改
name_lit[1] = "李四"
# list assignment index out of range
# 列表指定的索引超出范围，程序会报错！
# name_lit[2] = "王小二"

# 3.增加
# append可以向列表追加数据
name_lit.append("王小二")
# insert 方法可以在列表指定位置插入数据
name_lit.insert(1, "小美眉")
# extend 可以把其他列表中的完整类容，追加到当前列表末尾
temp_list = ["大师兄", "二师兄", "沙师弟"]
name_lit.extend(temp_list)

# 4.删除
# remove 方法可以从列表中删除指定的数据
name_lit.remove("wangwu")
# pop 方法默认可以吧列表中最后一个元素删除
name_lit.pop()
# pop 方法可以指定要删除的元素的索引
name_lit.pop(3)
# clear 方法可以清空列表
name_lit.clear()
print(name_lit)
