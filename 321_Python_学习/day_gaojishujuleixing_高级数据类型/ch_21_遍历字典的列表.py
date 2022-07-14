students = [
    {"name": "阿刚"},
    {"name": "建刚"}
]

# 在学员列表中搜索指定的名字
# find_name = "小建刚"

find_name = str(input("请输入要查找的姓名："))

for stu_dict in students:

    print(stu_dict)

    if stu_dict["name"] == find_name:

        print("找到了 %s " %find_name)

        # 如果已经找到， 应该直接退出循环，而不再遍历后续的元素
        break

    # else:
    #     print("抱歉没有找到 %s" % find_name)
else:
    # 如果希望在搜索列表时，所有的字典检查之后，都没有发现需要搜索的目标
    # 还希望得到一个统一提示
    print("抱歉没有找到 %s" % find_name)

print("循环结束")