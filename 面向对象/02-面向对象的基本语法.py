# 需求1
'''
小明今年18岁，身高1.75米，每天早上跑完步会去吃东西
小美今年17岁，身高1.65，小美每天不跑步，小美喜欢吃东西
'''
# 定义类:
'''
类名定义要遵守大驼峰命名法
 1.class <类名>:
 2.class <类名>(object):

'''

# self.var_name = var_name
# self.var_name 是内存里加的属性
# var_name 是对象传入的参数的值

# 什么是对象：对象就是内存里的一块空间

class Student(object):  # 关注这个类有哪些特征和方法
    # 在__init__方法里，以参数的形式定义特征，我们称之为属性
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    # 行为定义为一个个函数
    def run(self):
        print('正在跑步')

    def eat(self):
        print('正在吃东西')


# Student() ==> 会自动调用__init__方法
# 使用了Student类创建了两个实例对象s1、s2
# s1和s2都会有三个属性，同时都有run和eat方法
s1 = Student('小明', 18, 1.75)
s2 = Student('小美', 17, 1.65)

# 根据业务逻辑，让不同的对象执行不同的行为
s1.run()
s1.eat()

s2.eat()