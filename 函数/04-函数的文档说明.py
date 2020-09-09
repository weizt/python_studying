# 给函数写注释的方法
# python中对参数的数据类型没有限制
def add(a, b):
    '''
    这个函数表示将两个数字相加
    :param a: 表示第一个数字
    :param b: 表示第二个数字
    :return: 表示两个数据相加的结果
    '''
    return a + b


# 查看自定义函数的注释用help方法
help(add)
