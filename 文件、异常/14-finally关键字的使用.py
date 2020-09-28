# finally关键字：无论程序运行到什么程度，finally关键字后面的代码都会执行
file = open('names.txt', 'rb')
try:
    while True:
        content = file.read(1024)
        if not content:
            break
        print(content)
finally:  # 最终会执行的代码
    print('程序关闭了')
file.close()


# finally使用的注意事项
# try...finally...语句
# 一般情况下，一个函数最多只会执行一个return语句
# 特殊情况（finally语句）下，一个函数可能会执行多个return语句

def demo(x, y):
    try:
        z = x / y
    except ZeroDivisionError as error:
        return '除数不能为零'
    else:
        return z
    finally:
        # finally关键字return的结果会覆盖前一个return的结果
        return '我是finally的返回值'


print(demo(5, 2))
