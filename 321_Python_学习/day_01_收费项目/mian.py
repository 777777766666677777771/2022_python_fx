#! /usr/bin/python3

import gongneng

while True:

    gongneng.show_meun()

    action_str = input("请选择希望执行的操作: ")
    print("您选择的操作是 【%s】" % action_str)

    if action_str in ["1"]:

        if action_str == "1":
            gongneng.xianshi()

    elif action_str == "0":

        print("欢迎再次使用【空调安装计算费用系统V1.0】")

        break

    else :
        print("您输入的不正确，请重新输入")