# 调用模块时，不创建实例对象，使用model_name.function_name()的形式调用
class Person(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + '正在吃东西')


# 实现方法，先使用类名创建一个对象
p = Person('zhangsan')

# 再使用这个这个实例对象，直接调用这个方法，但不要加括号，给方法起一个别名
# 不加括号的函数，就是起一个别名
eat = p.eat

# 在调用时就可以直接使用。模块名.函数别名()
