class renlei:
    def __init__(self,name,gao):
        self.name = name
        self.gao = gao

    def __str__(self):
        return "名字 %s 体重 %.2f 公斤" % (self.name, self.gao)
    def run(self):
        print("%s 今天以完成跑步跟锻炼身体"% self.name)
        self.gao -= 0.5
    def set(self):
        print("%s 刚吃完东西，吃完这顿在减肥" % self.name)
        self.gao += 1
xiaoming = renlei("小明",55.0)
xiaoming.run()
xiaoming.set()
print(xiaoming)