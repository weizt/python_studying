# 需求：输入一个文件路径，然后拷贝一份相同的文件
'''
思路：
1.先打开旧文件
2.判断文件是否存在，如果存在则打开，os.path.isfile()方法判断
3.把旧文件的命名以元组的形式切片，可使用os.path.splitext()方法或者rpartition()方法
4.重命名新文件。把新文件名加上bak，bak为备份的缩写，默认使用
5.打开新文件，以写入的方式
6.写入内容为旧文件的内容
7。关闭新、旧文件

'''

'''
import os

file_name = input('输入一个文件路径：')
if os.path.isfile(file_name):

    old_file = open(file_name, encoding='utf8')
    # 名称切片方法一： rpartition('.')，以.分隔
    # names = file_name.rpartition('.')
    # print(names)
    # new_file_name = names[0]+'.bak.'+names[2]

    # 名称切片方法二：os.path.splitext()方法，将文件名以名称加后缀的形式隔开
    names = os.path.splitext(file_name)
    print(names)
    new_file_name = names[0] + '.bak' + names[1]
    new_file = open(new_file_name, 'w', encoding='utf8')
    new_file.write(old_file.read())

    old_file.close()
    new_file.close()
else:
    print('您输入的文件路径有问题')
'''

# 优化方案：以二进制的形式读取，以二进制的形式写入
# 方案优势：什么样的文件都可以拷贝
import os  # 导入os模块，以便后面调用path方法

file_name = input('输入一个文件路径：')
# 判断文件是否存
if os.path.isfile(file_name):

    # 以二进制的方式读取文件
    old_file = open(file_name, 'rb')

    # 调用splitext方法把原文件名切片
    names = os.path.splitext(file_name)
    print(names)

    # 新文件名的命名中间加’_bak‘
    new_file_name = names[0] + '_bak' + names[1]

    # 以二进制写入的形式打开新文件
    new_file = open(new_file_name, 'wb')
    while True:  # 使用循环1024的方式读取全部文件
        content = old_file.read(1024)  # 降低解析压力，释放内存空间
        new_file.write(content)  # 读一点写一点
        if not content:
            break

    old_file.close()
    new_file.close()
else:
    print('您输入的文件路径有问题')
