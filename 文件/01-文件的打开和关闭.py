# 在python里默认使用内置函数 open() 打开并操作一个文件
'''
参数介绍：
file:用来指定要打开的文件（这里指的是路径，不是文件名）
mode:打开文件时的模式，默认是 'r' ,表示只读
encoding:打开时的编码方式，在windows操作系统里默认的打开格式是'gbk'
open()函数会有一个返回值，打开文件的对象
'''


# UnicodeDecodeError 编码报错；解决方案：用相同的编码格式写入和读取
# python里打开文件路径用/
file = open('D:/桌面备份文件/207操作手册.txt', encoding='gbk')

print(file.read())

file.close()  # 文件操作完成后要记得关闭文件

