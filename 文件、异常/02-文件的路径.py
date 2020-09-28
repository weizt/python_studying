# 路径：绝对路径 和  相对路径
# 绝对路径：是从盘符开始的路径,详细的路径
# 相对路径：从当前路径开始的路径，简写的路径  推荐

# 技巧：右键点击文件名，打开Show in Explorer。直接打开文件位置
import os

print(os.sep)  # 在windows操作系里，文件夹之间用 \ 分隔；
# 而python中\表示字符串转义，所以会冲突

# 解决\冲突的三种方法
# 1.用两个\\表示一个\\
# 2.在字符串前加 r
# 3.在非windows系统用 / 推荐这一种

# file = open('D:\\桌面备份文件\\207操作手册.txt', encoding='gbk')
# file = open(r'D:\桌面备份文件\207操作手册.txt', encoding='gbk')
file = open('D:/桌面备份文件/207操作手册.txt', encoding='gbk')
print(file.read())


# 相对路径：当前文件所在的文件夹开始的路径。直接可以打开
file2 = open('01-文件的打开和关闭.py', encoding='utf8')
print(file2.read())


# ../ 表示返回到上一级文件夹
# ./ 可以省略不写，表示当前文件夹
file3 = open('./../requirements.txt', encoding='utf8')
print(file3.read())

file.close()
file2.close()
file3.close()