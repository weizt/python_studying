# pickle模块：将python里任意的对象转换成为二进制

import pickle

# pickle序列化方法：dumps:将Python数据转换成二进制
#                 dump：将Python数据转换成二进制，同时保存到指定的文件
# pickle反序列化方法：loads：将二进制数据加载成为Python数据
#                   load：读取文件，并将文件的二进制内容加载成为Python数据


names = ['张三', '李四', '王五', '牛二', '田七']
# 第一种dumps写入方法
'''
p = pickle.dumps(names)
print(p)
file_name = open('names.txt', 'wb')
file_name.write(p)
file_name.close()
'''

# 第一种loads加载方法
'''
file_name1 =open('names.txt','rb')
x = file_name1.read()
y = pickle.loads(x)
print(y)
file_name1.close()
'''

# 第二种dump方法,一步到位
file_name2 = open('names.txt', 'wb')
pickle.dump(names, file_name2)
file_name2.close()


# 第二种load加载方法,指定文件一步到位
file_name3 = open('names.txt', 'rb')
ppp = pickle.load(file_name3)
print(ppp)

file_name3.close()


# 强大之处在任意数据都可以转换
class Dog(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def eat(self):
        print(self.name + '正在吃东西')


dog1 = Dog('大黄', '白色')

file = open('dog.txt', 'wb')
# 保存文件
pickle.dump(dog1, file)  # 写入有乱码不用管
file.close()

# 加载文件
file2 = open('dog.txt', 'rb')
dd = pickle.load(file2)
dd.eat()
print(dd.name, dd.color)
