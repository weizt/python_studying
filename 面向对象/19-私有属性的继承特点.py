# 父类的私有方法，子类无法继承
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__bark = '吼吼吼' # 父类的私有属性，子类也无法继承

    def eat(self):
        print(self.name + '正在吃东西')

    def __test(self):
        print('我是父类的私有方法')


class Person(Animal):
    def __foo(self):
        print('我是子类的私有方法')


p = Person('张三', 19)
print(p.name)

p.eat()

# 子类的私有方法可以使用 对象名._子类名__私有方法名() 的方式调用
p._Person__foo()
# 也可以通过 对象名._父类名__私有方法名() 的方式进行调用
p._Animal__test()

# 父类的私有属性，子类无法继承
p._Person__test()  # AttributeError: 'Person' object has no attribute '_Person__test'==>

# 子类无法访问到父类的私有属性
print(p._Person__bark) # AttributeError: 'Person' object has no attribute '_Person__bark'
# 只能通过 对象名._父类名__私有属性名 的方式访问到父类的私有属性
print(p._Animal__bark)