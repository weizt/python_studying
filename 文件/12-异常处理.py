# 概念：在程序运行过程中，由于编码不规范造成程序无法正常执行，此时程序就会报错

def div(a, b):
    return a / b

# 导常格式
try:
    x = div(5 / 0)
    print('呵呵呵')
except Exception as error:  # 如果程序出错了，会立刻跳转到except语句
    print('程序出错了！！！')
else:  # 如果程序没有出错，会执行else里的代码
    print('计算的结果是', x)
