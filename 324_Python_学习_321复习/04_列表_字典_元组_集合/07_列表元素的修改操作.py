#
def xiugai():
    lst = [10, 20, 30, 40]
    # 一次修改一个值
    lst[2] = 100
    print(lst)
    lst[1:3] = [300,400,500,600] # 修改多个值
    print(lst)

xiugai()