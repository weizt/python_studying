# 概念：多态是基于继承，对它进行子类重写父类的方法，
#      达到不同的子类对象调用相同的父类方法，得到不同的结果
# 作用：提高代码的灵活度

# 需求：
'''
1.多种不同类型的狗
2.一个类型的人
3.同一个人与多种类型的狗做不同的工作
'''
# 思路
'''
1. 创建一个Dog类的父类
2. 定义不同Dog类的子类
3. 重写Dog类父类的方法
4. 人调用相同的方法名，实现不同的功能
5. Dog类定义不同的方法
6. Person类定义唯一的方法，此方法将调用不同的dog类的方法
'''


# 先定义一个Person
class Person(object):
    def __init__(self, name):  # Person类暂时不定义dog属性，默认为None
        self.name = name
        self.dog = None

    def with_work_dog(self):
        # 判断self.dog不为None，并且属性Dog类，则调用dog.work()方法
        if self.dog is not None and isinstance(self.dog, Dog):
            self.dog.work()


# 定义Dog类的父类
class Dog(object):
    def work(self):
        print('正在工作')


# 定义Dog类的子类
class SeeingEyeDog(Dog):
    # 重写父类的work()方法，以不同的子类，执行不同的结果
    def work(self):
        print('导盲犬正在指路')


class DetectionDog(Dog):
    # 重写父类的work()方法，以不同的子类，执行不同的结果
    def work(self):
        print('缉毒犬正在缉毒')


class PoliceDog(Dog):
    # 重写父类的work()方法，以不同的子类，执行不同的结果
    def work(self):
        print('警犬正在抓捕坏人')


# 创建一个Person的实例对象，再创建一个Dog类实例对象，并加动态属性dog

p = Person('张三')

# 创建Dog子类的实例对象
sed = SeeingEyeDog()
# 将此对象赋值给Person类的self.dog属性
p.dog = sed
# 调用并执行Person类的with_work_dog()方法
p.with_work_dog()

dd = DetectionDog()
p.dog = dd
p.with_work_dog()

pd = PoliceDog()
p.dog = pd
p.with_work_dog()
