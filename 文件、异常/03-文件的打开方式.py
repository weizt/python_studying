# 文件的打开方式：mode:打开文件时的模式，默认是 'r'
# 1.r:只读模式，不能写入;文件不存在时会报错
# 2.w：写入模式：打开文件后，只能写入，不能读取。如果文件存在，会覆盖文件，如果文件不存在，会创建文件
# 3.b：以二进制的形式打开文件（可以操作非文字类型文件）
#      rb表示以二进制的方式读取
#      wb表示以二进制的方式写入

# file = open('D:/桌面备份文件/207操作手册.txt', encoding='gbk')
# print(file.read())

file2 = open('file_test.txt', 'w', encoding='utf8')
file2.write('这是测试文件一')

file2 = open('file_test.txt', 'wb')
file2.write('这是有wb方式写入'.encode('utf8'))  # wb模式必须将str类型改为二进制写入
file2.close()
