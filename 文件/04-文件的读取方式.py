# file = open('D:/桌面备份文件/207操作手册.txt', encoding='gbk')

# readline() 只读取一行
# print(file.readline())

# 如果想读取多行，可以用下面的方法
# while True:
#     countent =file.readline()
#     print(countent)
#     if countent == ''
#         break

# readlines() 将读取所有行的数据，保存到一个列表里
# x = file.readlines()
# print(x)


# 指定长度的读取
# file.read(104) 不以rb形式读取，就是读取字数

# 找荐使用这一种方式循环读取，二进制，每次读取1024字节，以节省内存
file = open('D:/华宇互联网庭审使用介绍（发布版）.wmv', mode='rb')
while True:
    content = file.read(1024)
    if not content:
        break
    print(content)

file.close()
