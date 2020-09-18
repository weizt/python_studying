'''
房子(House) 有户型、总面积、剩余面积（总面积的60%）和家具名称列表 属性
新房子没有任何家具
将家具的名称追加到家具名称列表中
判断家具的面积是否超过剩余面积，如果超过，提示不能添加这件家具

家具(Furniture) 有名字 和占地面积属性，其中
席梦思(bed) 占地 4 平方米
衣柜(chest) 占地 2 平方米
餐桌(table) 占地 1.5 平方米
将以上三件 家具添加到房子中
打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
'''


# 1.创建房子类
class House(object):  # 不建议属性为空的可迭带对象，建议属性定义为None，用if语句判断生成空列表等
    def __init__(self, house_type, total_area, fur_list=None):
        if fur_list is None:
            fur_list = []
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area * 0.6
        self.fur_list = fur_list

    # 1.1 在房子类中定义添加家具的方法，并且定义一个参数，参数=家具
    def add_fur(self, furs):
        if self.free_area < furs.fur_area:
            print('总面积是{}平方米，户型是{}，无法再添加{}这件家具了'.format(self.total_area, self.house_type, furs.fur_name))
        else:
            self.fur_list.append(furs.fur_name)
            self.free_area = self.free_area - furs.fur_area

    # 1.2 重定义__str__方法，输出对象的内容,要定义返回值，不能写print
    def __str__(self):
        return (
            '户型是{}，房子的总面积是{}平方米，剩余面积是{}平方米，家具有{}'.format(self.house_type, self.total_area, self.free_area,
                                                         self.fur_list))


# 2.创建家具类
class Furniture(object):
    def __init__(self, fur_name, fur_area):
        self.fur_name = fur_name
        self.fur_area = fur_area


# 3.创建房子的实例对象
house = House('三室两厅', 120)
house2 = House('一室一厅', 50)

# 4.创建家具的实例对象
sofa = Furniture('沙发', 40)
bed = Furniture('席梦思', 4)
chest = Furniture('衣柜', 2)
table = Furniture('餐桌', 1.5)

# 5 调用add_fur方法，把家具添加到房子里。（面向对象的关注点：让谁做）
house.add_fur(sofa)
house.add_fur(bed)
house.add_fur(chest)
house.add_fur(table)

# 6.打印这个房子,不能直接打印对象，要打印对象，相当于调用对象的__str__或者__repr__方法
print('house的', house)

house2.add_fur(sofa)
house2.add_fur(bed)
house2.add_fur(chest)
house2.add_fur(table)
print('house2的', house2)
