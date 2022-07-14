'''
输出100到999之间的水仙花数
    举例：
    153 = 3 * 3 * 3 + 5 * 5 * 5 + 1 * 1 * 1
'''

for itme in range(100, 1000):
    ge = itme % 10 # 个位
    shi = itme//10%10 # 十位
    bai = itme//100 # 百位
    # print(bai, shi, ge)
    # 判断
    if ge**3+shi**3+bai**3==itme:
        print(itme)
