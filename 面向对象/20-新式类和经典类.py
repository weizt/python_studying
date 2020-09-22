# 定义类时，加(object)与不加是一样的

# 手动的指定Student类继承自object
class Person(object):
    pass

# 没有指定父类，python3里默认继承自object
class Animal:
    pass

# 新式类和经典类的概念
'''
1.新式类:继承自object的类，我们称之为新式类
2.经典类：不继承自object的类，我们称之为经典类
3.在python2里，如果不手动指定一个类的父类是object，这个类就是一个经典类
4.python3中里不存在经典类和新式类，默认都是继承object类
'''