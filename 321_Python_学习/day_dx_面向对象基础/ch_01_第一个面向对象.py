class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()
tom.eat()
tom.drink()

print(tom)

addr = id(tom)
# 注意： 在计算机中， 通常用十六进制 表示 内存地址
print("%x" % addr)   # %x 十六进制
print("%d" % addr)   # %d 十进制