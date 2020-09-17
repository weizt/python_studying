class Student(object):
    def __init__(self, x, y):
        self.name = x
        self.age = y

    def say_hello(self):
        print('大家好，我是', self.name)


s1 = Student('zhangsan', 18)
# s1 = Student('zhangsan',18) 这段代码的运行逻辑
'''
1.调用__new__方法，用来申请内存空间
2.调用__init__方法，传入参数，将self指向创建好的内存空间，填充数据
  注意：此时内存中传入的变量名为name.和age，不是x,y
3.变量s1也指向创建好的内存空间
'''
print('s1的的名字是', s1.name)
print('0x%X' % id(s1))

# 哪个变量调用say_hello函数，针对的对象就是本身
s2 = Student('lisi', 19)
s2.say_hello()

# 如果执行这个实例对象没有的属性，会报错
# print(s1.height)  ==>AttributeError: 'Student' object has no attribute 'height'


# 如果用等于号给实例对象赋值了一个新属性和对应的值
# 如果这个属性之前不存在，相当于添加了新属性
# 如果这个属性之前存在，会修改这个属性对应的值
s1.city = '上海'  # 这个叫动态属性，其他语言一般不允许
print(s1.city)
