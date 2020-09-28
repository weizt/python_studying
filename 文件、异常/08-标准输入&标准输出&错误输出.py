import sys

# 可以像inpu#t一样，接收用户的输入，和input相关
# sys.stdin

# 修改sys.stdout，可以改变默认输出的位置
# sys.stdout

# 修改sys.stderr，可以改变错误输出默认位置
# sys.stderr


# 标准输入,在控制台里实现不停的输出
s_in = sys.stdin
while True:
    content = s_in.readline().strip('\n')
    if content == '':
        break

    print(content)

# 标准备输出，把输入内容打印到另的位置
# 把原来输出在控制台的内容转移到一个文件内，以后每次打印的内容，都会出现
sys.stdout = open('stdout.txt', 'w', encoding='utf8')
print('这是测试sys.stdout')
print(11111)


# 把控制台的错误输出提示转移到另一个文件当中，相当于打印错误日志
sys.stderr = open('error.txt', 'w', encoding='utf8')
print(1 / 0)
