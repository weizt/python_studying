class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 如果重写了__eq__方法,并且返回两个对象的值是全等的,那么 == 相比较将变成True
    def __eq__(self, other):
        print('__eq__方法被调用了,other=', other)
#       return self.name == other.name and self.age == other.age


p1 = Person('zhangsan', 18)
p2 = Person('zhangsan', 18)

# 比较两个对象否为同一个,要比较内存地址
print('0x%X' % id(p1))
print('0x%X' % id(p2))

# is 身份运算符
# 通过比值对象的内存地址
# 可以用来判断是否为同一对象
print(p1 is p2)  # False

# ==会调用对象的__eq__方法,如果不重写,默认比较的依然是内存地址
print(p1 == p2)  # ==> False   实际就是调用p1.__eq__(p2)
