# 创建一个Person类
class Person(object):
    type = '人类'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # eat()函数在保存在类对象的内存中的
    def eat(self, food):  # 对象方法有一个参数self,指的就是实例对象
        print(self.name + '正在吃' + food)

    # 当一个方法里没有用到实例对象的任何属性，可以将这个方法写static
    # 创建格式  @staticmethod ，每个静态方法都要加@staticmethod
    #          def <function>()
    #              pass
    @staticmethod
    def deom():  # 这是一个静态方法
        print('我是静态方法')

    # 当一个函数只用到了类属性，可以定义为一个类方法
    # 类方法会有一个参数cls，不需要手动传参，自动传参
    # cls指的就是类对象
    @classmethod
    def test(cls): # cls is Person
        print(cls.type)
        print('我是一个类方法')




p1 = Person('张三', 18)
p2 = Person('李四', 19)

# 当使用实例对象调用实例方法时，使用 实例对象名.函数名() 的方式
# 这其中 self 这个形参是自动传参，将自动把实例对象传递给 self
# 所有只需要写一个参数即可
p1.eat('红烧牛肉面')  # self ==> 自动传入

# 不同的实例对象调用相同的实例方法，会形成不同的绑定空间存储在内存之中
# 所以 p1.eat() is p2.eat()  ==> False
p2.eat('韭菜炒鸡蛋')

# 而当类对象直接调用实例函数时，刚需要手动传参给self
# 所以调用方法为 类名.函数名(实例对象,实参) self ===> 实例对象参数  必须手动传递
Person.eat(p1, '蛋炒饭')

# 静态方法的调用
Person.deom()  # <类名>.<函数名>()
p1.deom()  # <p实例对象名>.<函数名>()

# 类方法的调用
Person.test()  # <类名>.<类函数名>()
p1.test()  # <p实例对象名>.<类函数名>()