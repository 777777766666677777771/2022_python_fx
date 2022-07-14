for num in [1, 2, 3, 4, 5, 6]:

    print(num)
    if num == 5:
        break
else:
    # 如果循环体内部使用break退出了循环
    # else  下方代码就不会被执行
    print("会执行吗？")

print("循环结束")