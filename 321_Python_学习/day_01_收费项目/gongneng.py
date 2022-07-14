# 全局变量 安装费， 材料费， 高空费
pishu = ["1匹1.5匹", "2匹3匹"]
anzhuang_jk_1_15 = 150
anzhuang_jk_2_3 = 250
gaokongfei = 100
ciliao_tongguan_6_10 = 100
ciliao_tongguan_6_12 = 110
ciliao_tongguan_6_16 = 120
ciliao_tongguan_10_16 = 150
ciliao_kongkai = 90
ciliao_buxuigangzhijia_1_15 = 80
ciliao_buxuigangzhijia_1_2 = 120
ciliao_buxuigangzhijia_1_3 = 150
ciliao_fangzhengxian = 60


def xianshi():

    print("欢迎使用空调收费计算系统 - 版本V1.0")
    print("*" * 50)
    print("【高空费-安装费】")
    print("\t1到3匹---4楼及以上：100 $台 200封顶")
    print(" ")
    print("\t1到1.5匹 空调安装费  %d $台"% anzhuang_jk_1_15)
    print("\t2到3匹 空调安装费 %d $台" % anzhuang_jk_2_3)
    print("\t（有高空算高空）")
    print("【材料】 ")
    print("\t铜管 6/10: %d $米" % ciliao_tongguan_6_10)
    print("\t铜管 6/12: %d $米" % ciliao_tongguan_6_12)
    print("\t铜管 6/16: %d $米" % ciliao_tongguan_6_16)
    print("\t铜管 10/16: %d $米" % ciliao_tongguan_10_16)
    print("\t不锈钢支架 1匹和1.5匹: %d $个" % ciliao_buxuigangzhijia_1_15)
    print("\t不锈钢支架 2匹: %d $个" % ciliao_buxuigangzhijia_1_2)
    print("\t不锈钢支架 3匹: %d $个" % ciliao_buxuigangzhijia_1_3)
    print("\t防震垫： %d $套" % ciliao_fangzhengxian)
    print("\t漏电保护空开: %d个 $" % ciliao_kongkai)
    print("*" * 50)


def show_meun():

    """显示菜单"""
    print("*" * 50)
    print("欢迎使用（空调安装计算费用系统）V1.0")
    print("")
    print("1. 显示收费详情")
    print("")
    print("0 .退出系统")
    print("*" * 50)


def show_all():

    print("-" * 50)
    print("显示收费标准")

    xianshi()

def jisuan():

    a = input("请输入： 匹数")









