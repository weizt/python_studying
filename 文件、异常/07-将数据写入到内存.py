# 将数据写入到内存涉及到 StringIO和BytesIO两个类
from io import StringIO, BytesIO

s_io = StringIO()
s_io.write('hello')  # 把数据写入到内存里
s_io.write('good')
s_io.write('yes')

# 把内存里的数据都一次性打印出来
print(s_io.getvalue())

# repr()把数据转换成字符串
a = 2222
repr(a)  # ==> '222'
print(type(repr(a)))

# print() 的file 参数的使用,file需要的是一个文件流对象
print('weizhetao', file=s_io)
print('raoyue', file=s_io)
print('weimile', file=s_io)
print(s_io.getvalue())

s_io.close()

# BytesIO的用法
b_io = BytesIO()
b_io.write('你好'.encode('utf8'))  # 写入时用二进制写入
print(b_io.getvalue().decode('utf8'))  # 读取时要解码二进制读取

b_io.close()