"""qyan = "超市购买结算系统"
print(qyan)
print("-" * 50)
jr = input("请输入今日的苹果多少钱一斤：")
gm = input("请输入要购买的斤数：")

# “float函数” 作用 转换 “jr” 字符串 为 浮点数 进行 计算
jr1 = float(jr)
gm1 = float(gm)
zj = jr1 * gm1
print("付款总金额为 %s" % zj)"""

#  高级版
jr = float(3.2)
print("今天苹果3.2/斤")
print("-" * 50)
gm = float(input("请输入要购买的斤数："))

zj = jr * gm
print("苹果的单价 %0.2f/斤 你购买了 %0.2f/斤 需要付款 %0.2f/元" % (jr, gm, zj))