# 序列化：将数据从内存持久化保存到硬盘的过程
# 反序列化：将数据从硬盘加载到内存的过程

# write方法：只能只写入字符串或者二进制，无法写入数据、列表、元组等等
# 使用repr()或str()方法将数据转换成字符串；将数据转换成二进制

# 最常用方法：使用json模块转换
# 或者使用pickle模块转换为字符串
# json本质就是字符串，区别在于json里要用双引号表示字符串
# 总结：json.dumps()，转换json字符串，并不保存；json.dump(),把数据转换成json字符串，并保存到指定位置
#      josn.loads()，把json字符串转换成pyhton字符串; josn.load()打开一个json字符串文件，并转换成一个python对象


import json

file = open('name.txt', 'w', encoding='utf8')
name = ['zhangsan', 'lisi', 'wangwu', 'jack']

# json.dumps()方法:作用就是将数据转换成字符串,不会将数据保存到文件
# x = json.dumps(name)
# file.write(x)

# json.dump()方法:次数转换成为json字符串的同时写入到指定文件
# 指定要写入的数据，指定数据保存的文件名
json.dump(name, file)
file.close()

# json反序列化两个方法
# loads:将json字符串加载成为python里的数据
# load:读取文件，把读取的内容加载成为python里的数据


# 符合json规则的字符串
x = '{"name":"zhangsan","age":18}'
p = json.loads(x)  # 把json字符串转变为Ptyhon数据
print(p)
print(p['name'])

file1 = open('name.txt', 'r', encoding='utf8')
# load 读取一个文件，并把文件里json字符串加载成为一个对象
y = json.load(file1)
print(y)
print(y[0])

file1.close()

# 非python规则类转换成json类，会报错
