chepiao = True
dao  = int(input("请输入刀的长度："))
if chepiao:
    print("有车票")
    if dao >= 40:
        print(("但你的刀太长了，不可以携带, 你的刀长 %d 公分" % dao))
    else:
        print("符合规定")
        print("欢迎乘坐")
else:
    print("您没有车票")