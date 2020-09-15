# sys系统相关的功能
import sys

# 结果是一个列表，表示查找模块的路径
print(sys.path)

# 可以像input一样，接收用户的输入，和input相关
sys.stdin

# 修改sys.stdout，可以改变默认输出的位置
sys.stdout

# 修改sys.stderr，可以改变错误输出默认位置
sys.stderr
# 程序退出，和内置函数exit()功能一致
sys.exit()  # 可以输入一个任意的退出码，如100，默认为0
