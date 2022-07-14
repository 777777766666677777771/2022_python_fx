def lst_index():
    lst = ['hello', 'python', 98, 'hello', 'hello', 'python']
    print(lst.index('hello')) # 如果列表中有相同元素，只返回列表中相同元素的第一个元素的索引
    # print(lst.index('礼拜')) # ValueError: '礼拜' is not in list
    # print(lst.index('hello', 1, 3)) # ValueError: 'hello' is not in list
    print(lst.index('hello', 1, 4))  # 在指定范围查找数据索引


def lst_dange_index():
    lst = ['hello', 'world', 98, 'hello', 'world', 234]
    # 希望获取索引唯2的元素
    print(lst[2])
    # 希望获取索引唯-3的元素
    print(lst[-3])
    # 希望获取索引唯10的元素
    print(lst[10])



# lst_index()
lst_dange_index()