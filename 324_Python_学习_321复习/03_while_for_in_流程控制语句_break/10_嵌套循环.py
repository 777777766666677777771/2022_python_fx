# 输出一个三行四列的矩形
def juxing():
    for i in range(1,4): # 行表： 执行3次， 一次是一行
        for j in range(1,5):
            print('*', end='\t') # 不换行输出
        print() # 打行


# 输出乘法口诀表
def sanjiao():
    for i in range(1,10): # 行数
        for j in range(1,i+1):
            print(i,'*',j,'=', i*j ,end='\t')
        print()


# juxing()
sanjiao()
