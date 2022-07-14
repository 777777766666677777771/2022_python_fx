#  在控制台打印5行小星星，每一行依此递增！
#
row = 1
while row <= 9:
    col = 1
    while col <= row:
        # print("%d " % col)
        print("*", end="")
        col += 1
    # print("第一次：%s " % row)
    print("*")
    row += 1
