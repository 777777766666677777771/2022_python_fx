class Hostjiaju:

    def __init__(self, name, area):
        self.name = name
        self.area = area
    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)

class fangzi:
    def __init__(self, type, area):
        self.type = type
        self.area = area


bed = Hostjiaju("席梦思", 4)
yikui =Hostjiaju("衣柜", 2)
kongtiao = Hostjiaju("空调", 5)
print(bed)
print(kongtiao)
print(yikui)