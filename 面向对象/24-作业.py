'''
设计两个类：
一个点类：属性包括x,y坐标
一个Rectangle类（矩形）:属性有左上角和右下角的坐标
方法：1.计算矩形的面积；2.判断点否是矩形内
实例化一个点对象，一个矩形对象，输出矩形的面积，输出点是否在矩形内
'''


# 创建Point类，有x,y两个坐标参数；参数类型是int类
class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


# 创建Rectangle矩形类，有左上角和左下角两个坐标参数；参数类型是Point类
class Rectangle(object):
    def __init__(self, left_top: Point, right_bottom: Point):
        self.left_top = left_top
        self.right_bottom = right_bottom

    # 定义get_area方法用来获取面积 长*宽
    def get_area(self):
        length = abs(self.right_bottom.x - self.left_top.x)
        width = abs(self.left_top.y - self.right_bottom.y)
        return length * width

    # 定义judge判断方法用来判断点是否在矩形对象内，参数为Point对类
    def judge(self, Point):
        # if self.left_top.x <= Point.x <= self.right_bottom.x and self.right_bottom.y <= Point.y <= self.left_top.y:
        #     return True
        # else:
        #     return False
        # 简化写法
        return self.left_top.x <= Point.x <= self.right_bottom.x and self.right_bottom.y <= Point.y <= self.left_top.y


p1 = Point(4, 20)
p2 = Point(30, 8)

area = Rectangle(p1, p2)
print(area.get_area())

p3 = Point(4, 15)
print(area.judge(p3))

'''
创建一个Person类，添加一个类字段用来统计Person类对象的个数
'''


class Person(object):
    __count = 0  # 定义一个私有类属性用来计数

    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        return object.__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod  # 创建私有类方法，调用时
    def get_count(cls):
        return ('创建了{}个实例对象'.format(cls.__count))


p1 = Person('111', 2)
p2 = Person('111', 2)
p3 = Person('111', 2)
p4 = Person('111', 2)

print(Person.get_count())

'''
建立一个汽车类Auto，包括轮胎个数，汽车颜色，车身重量，速度等属性，并通过不同的构造方法创建实例。
至少要求汽车能够加速、减速、停车。再定义一个小汽车类CarAuto，继承Auto并小添加空调，CD属性，并且
重新实现方法覆盖加速、减速的方法
'''


class Auto(object):
    def __init__(self, color, car_weight, speed=0, wheel_num=4):
        self.color = color
        self.car_weight = car_weight
        self.speed = speed
        self.wheel_num = wheel_num

    def speed_up(self, x: int):
        if x > 0:
            self.speed += x
            return ('此车正在以{}km/h的加速行驶'.format(self.speed))
        else:
            return ('车速为{}，车速保持不变'.format(self.speed))

    def speed_down(self, x: int):
        if x < 0:
            self.speed += x
            return ('此车正在以{}km/h的减速行驶'.format(self.speed))
        else:
            return ('减速为{}，车速保持不变'.format(self.speed))


class Car(Auto):
    def __init__(self, color, car_weight, ac, cd, speed=0, wheel_num=4):
        self.ac = ac
        self.cd = cd
        super(Car, self).__init__(color, car_weight, speed, wheel_num)


car = Auto('红色', 1.6)
# print(car.speed_up(0))
# print(car.speed_up(30))

print(car.speed_down(-10000))

car1 = Car('红色', 1.9, '海尔', 'ios', 50, 3)
print(car1.cd)
print(car1.ac)
print(car1.speed)
print(car1.wheel_num)
