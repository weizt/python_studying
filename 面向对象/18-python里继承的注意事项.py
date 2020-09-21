# 如果类不写()，默认以object为父类
# python里允许多继承：class 子类名(父类1,父类2...)
# 多继承可以传递
# 如果子类继承了多个父类，且不同父类中有同方法，则调用优先级为父类1的顺序先往上查找，如果没有，再找父类2的顺序往上查找，以此类推
# 类属性有一个类属性查以查看优先级 类名.__mor__
class A(object):
    def deom_a(self):
        print('我是demo_a方法')


class B(object):
    def deom_b(self):
        print('我是demo_b方法')


class C(A, B):
    def __init__(self):
        pass


c = C()
c.deom_a()
