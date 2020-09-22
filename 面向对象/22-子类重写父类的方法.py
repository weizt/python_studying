# 子类与父类方法同名，但功能不一样，推荐子类重写
# 子类在父类方法的基础上，想拥有更多实现，推荐使用super(子类名,self).方法名(参数1，参数2)调用相同的部分

# 定义一个类
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')


# 定义一个子类，继承自父类

class Student(Person):
    # 子类与父类有同名方法，但功能不一样，子类可以重写这个方法，同名方法，子类优先级最高

    def __init__(self, name, age, school):  # 子类重写父类同名方法，并加入多个参数
        # self.name = name  太冗余，与父类重复
        # self.age = age    太冗余，与父类重复
        # 调用父类相同方法的两种方式
        # 1. 父类名.方法名(self,参数1，参数2...)
        # Person.__init__(name, age) 等同于  self.name = name
        #                                   self.age = age
        # 2. 使用super直接调用父类的方法。推荐第二种
        super(Student, self).__init__(name, age)  # 等同于   self.name = name
                                                  #         self.age = age

        self.school = school  # 再加自己想要的参数或者功能

    def sleep(self):  # 子类重写sleep方法，直接在子类重新定义一个同名方法，功能自定
        print(self.name + '在' + self.school + '上课期间不允许睡觉')


p = Student('张三', 18, '春田花花幼儿园')
p.sleep()  # 不强调类对象，则子类优先级最高
Person.sleep(p)
Student.sleep(p)
