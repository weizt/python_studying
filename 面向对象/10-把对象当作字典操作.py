class Person(object):
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __setitem__(self, key, value):
        # 先使用__dict__方法把对象变成字典，再通这修改字典的键-值对方式来修改
        self.__dict__[key] = value

    def __getitem__(self, item):
        # 使用__getitem__方法把对象当作字典获取值
        return self.__dict__[item]


p = Person('张三', 19, '上海')

# 以字典的形式打印p这个实例对象
print(p.__dict__)

# 想把对象当作字典来操作，可以使用__setitem__魔术方法。
# 本质上只要使用了[]，就会自动调用这个方法，我们需要做的就是重新义这个方法，使之可以成为字典使用
p['name'] = '李四' # 可以当作字典修改值了
p['city'] = '北京'
print(p.name)
print(p.city)
print(p.__dict__)

# 把对象当作字典通过key获取value,使用__getitem__方法，第11行
print(p['name'])

