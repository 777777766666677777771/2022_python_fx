class renlei:
    def __init__(self,name,gao):
        self.name = name
        self.gao = gao

    def __str__(self):
        return "名字 %s 体重 %.2f 公斤" % (self.name, self.gao)
    def run(self):
        print("%s 今天以完成跑步跟锻炼身体"% self.name)
        self.gao -= 2
    def set(self):
        print("%s 刚吃完东西，吃完这顿在减肥" % self.name)
        self.gao += 1

xiaoming = renlei("小明",88)

xiaoming.run()
xiaoming.set()
print(xiaoming)

# 小美也爱跑步吃东西
xiaomei = renlei("小美",40)
xiaomei.set()
xiaoming.run()

print(xiaomei)
