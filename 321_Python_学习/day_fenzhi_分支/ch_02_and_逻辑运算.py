# 1:一个整数变量age，写代码来确定一个年龄是否合适年龄=

# 120#对于年龄为0-120岁的人
age = int(input("请输入年龄："))
if age >= 0 and age <= 120:
    print("年龄正确")
else:
    print("年龄不够")
