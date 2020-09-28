# 概念：除了系统内置的异常，还可以 raise 关键字自定义异常
# 自定义异常的格式：
'''
1.定义一个异常类
2.重写异常类的__init__方法和__str__方法
'''


# 需求：让用户输入用户名和密码，如果用户名的密码长度在6~12位正确，否则不正确

class LengthError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '长度必须在{}和{}之间'.format(self.x, self.y)
        # 自定义异常输出的内容


password = input('请输入你的密码：')
m = 6
n = 12
if m <= len(password) <= 12:
    print('密码正确')
else:
    raise LengthError(m, n)
# 使用raise抛出一个异常
