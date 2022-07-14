# i = 0
#
# while i < 10:
#         # j = 0
#         # while j
#
#     if i == 4:
#         #  break 条件满足，触发break,强制退出循环
#         break
#     print(i)
#     i += 1
# print("结束了")

j = 0
while j <= 9:
    if j == 3:
        j += 1
        #  continue 条件满足， 触发continue,跳过if指定循环，继续执行循环
        continue
    print(j)
    j += 1
print("结束了")
