# 数据类型
# 常用的数据类型
    # 整数类型 -> :int --->98   - 可以表示，正数，负数，0
def int():
    n1 = 90
    n2 = -76
    n3 = 0
    print(n1, type(n1))
    print(n2, type(n2))
    print(n3, type(n3))
    # 整数 可以表示为二进制， 十进制， 八进制， 十六进制
    print("十进制", 118)   # 十进制->默认的进制
    print("二进制", 0b1010111)     # 二进制->以0b开头
    print("八进制", 0o176)     # 八进制->以0o开头
    print("十六进制", 0x1EAF)  # 十六进制->以0x开头

    """
90 <class 'int'>
-76 <class 'int'>
0 <class 'int'>
十进制 118
二进制 87
八进制 126
十六进制 7855
************************************************** 整数类型
    """

    # 浮点数类型 -> :float --->3.14159
def float():
    a = 3.14159
    print(a, type(a))
    n1 = 1.1
    n2 = 2.2
    n3 = 2.1
    print(n1 + n2)
    print(n1 + n3)
    from decimal import Decimal
    print(Decimal("1.1") + Decimal("2.2"))

    # 布尔类型 -> :bool ---> TRUE, FALSE
    """用来表示真或假的值
    TRUE表示真， FALSE表示假
    布尔值可以转化为整数"""
        # TRUE->1
        # FALSe ->0

    """
3.14159 <class 'float'>
3.3000000000000003
3.2
3.3
************************************************** 浮点数类型
    """

def bool():

    f1 = True
    f2 = False
    print(f1, type(f1))
    print(f2, type(f2))
    # 布尔类型可以转成整数计算
    print(f1+1) #2  1+1的结果为2， TRUE表示1
    print(f2+1) #1  0+1的结果为1， FALSE表示0

    # 字符串类型 -> :str ---> "7671"， "昌韵"

    """
True <class 'bool'>
False <class 'bool'>
2
1
************************************************** 布尔类型
    """

def str():

    str1 = '随便字符串'
    str2 = "随便字符串"
    str3 = """随便
    字符串"""
    str4 = '''随便
    字符串'''
    print(str1, type(str1))
    print(str2, type(str2))
    print(str3, type(str3))
    print(str4, type(str4))

    """
随便字符串 <class 'str'>
随便字符串 <class 'str'>
随便
    字符串 <class 'str'>
随便
    字符串 <class 'str'>
************************************************** 字符串类型
    """

int()
print("*" * 50, "整数类型")
float()
print("*" * 50, "浮点数类型")
bool()
print("*" * 50, "布尔类型")
str()
print("*" * 50, "字符串类型")
