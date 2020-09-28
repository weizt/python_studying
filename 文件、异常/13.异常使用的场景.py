# try...except... 语句用来处理程序运行过程中的异常
try:
    file = open('ddd.txt')
    print(file.read())
    file.close()
except Exception as error:  # 给异常起一个变量名 error
    print(error)

# 手动添加指定错误类型

try:
    file = open('ddd.txt')
    print(file.read())
    file.close()
except (ArithmeticError, NameError, FileNotFoundError) as error:  # 用元组添加多个异常类型
    print(error)

# 异常使用场景示例
age = input('请输入您的年龄:')

try:
    age = float(age)
except ValueError as error:
    print('您输入的不是数字')
else:
    if age >18:
        print('欢迎您来到的我的网站')
    else:
        print('未成年人禁止入内')
