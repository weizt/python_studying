# isinstance用来判断一个对象是否是由指定的类或者父类实例化出来的
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Person(object):
    pass


class Student(Animal, Person):
    pass


p = Animal('张三', 19)

# 用isinstance来判断一个实例对象是否由指定的类或者父类实例化
# 有来元组包含多个被比较类
print(isinstance(p, (Animal, Person)))  # ==> True

# issubclass用来判断一个类是否是另一个类的子类
# 也可以用元组比较多个类
print(issubclass(Student, Animal))  # ==> True
