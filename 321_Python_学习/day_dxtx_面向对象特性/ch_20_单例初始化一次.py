class MuiscPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None

    # 记录是否执行过初始化动作
    init_false = False

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2. 调用父类的方法， 为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):

        # 1. 判断是否执行过初始化动作
        if MuiscPlayer.init_false:
            return

        # 2. 如果没有执行过，在执行初始化动作
        print("初始化播放器")

        #3. 修改类属性的标记
        MuiscPlayer.init_false = True

# 创建多个对象
player1 = MuiscPlayer()
print(player1)

player2 = MuiscPlayer()
print(player2)



