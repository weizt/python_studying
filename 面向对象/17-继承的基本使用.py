# 子类(派生类)继承父类(基类)的概念
# class <父类名>(object):  父类
#   pass

# class <子类名>(父类名)：子类继承 在括号父类名
#   pass

class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')


class Dog(Animal):
    def bark(self):
        print(self.name + '正在叫')


class Student(Animal):
    def study(self):
        print(self.name + '正在学习')


'''
过程：
    子类优先调用自己的__new__方法，再调用__init__方法
    如果没有，则查出父类是否重写了__new__方法和__init__方法
    如果父类也没有重写，就查找父类的父类，找到object
'''


dog = Dog('大黄', 3)
dog.sleep()
dog.bark()

student = Student('小明', 18)
student.sleep()
student.study()
