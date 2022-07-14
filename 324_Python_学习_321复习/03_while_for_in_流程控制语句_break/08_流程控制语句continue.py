# 要求输出1到50之间所有5的倍数， 5，10，15，20，25....
# 5的倍数的共同点是什么： 和5的余数为0的数都是5的倍数
# 什么样的数不是5的倍数 1， 2， 3， 4， 5， 6... 与5的余数不为0的数都不是5的倍数
# 要求使用continue实现
for item in range(1, 50):
    if item%5==0:
        print(item)

print('-----------------使用continue-------------')
for item in range(1, 50):
    if item%5!=0:
        continue
    print(item)