# 列表有几个内置函数和内置类，用到了匿名函数
nums = [4, 8, 1, 5, 6, 2, 3, ]
# sort方法进行排序,会直接对列表进行排序
# 所以不能直接打印
nums.sort()
print(nums)

# sorted内置函数，不会改原有的数据，而是生成一个新的有序列表
nums1 = [11, 66, 55, 33, 44, 22, 55, 99, 88]
# 可以直接打印
print(sorted(nums1))

students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': '180cm'},
    {'name': 'lisi', 'age': 28, 'score': 100, 'height': '170cm'},
    {'name': 'wangwu', 'age': 23, 'score': 90, 'height': '196cm'},
    {'name': 'jack', 'age': 21, 'score': 88, 'height': '176cm'},
    {'name': 'hoeny', 'age': 19, 'score': 65, 'height': '163cm'}
]


# TypeError: fun() takes 0 positional arguments but 1 was given
# fun这个函数需要0个参数，但是调用时传入了一个参数，所以报错
# def fun():
#     pass


def fun1(ele):
    print('ele={}'.format(ele))  # 查看调用参数时，拿谁作为比较对象


def fun(ele):
    return ele['age']


students.sort(key=fun)  # sort内置函数可以传入参数，参数必须是函数
print(students)

# 使用lambda函数简化写法
students.sort(key=lambda ele: ele['age'])
print(students)
