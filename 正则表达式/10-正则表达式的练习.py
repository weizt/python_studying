# 判断用户输入的内容是否为数字，如是数字转换成数字类型
import re

num = input('请输入一个数字：')
if re.fullmatch(r'\-?\d+(\.?\d+)?', num):  # 首位是数字，可以出现1次或多次，中间是点，可以出现0次或1次，后面为数字，可以出现1次或多次
    print('这是一个数字')
    print(float(num))
else:
    print('这不是一个数字')

# 邮箱的正则表达式
email = 'weizhetao@163.com'
x = re.fullmatch(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email)
print(x)

idcard = '34252219931117091X'
y = re.fullmatch(r'^[1-9]\d{5}(18|19|20|(3\d))\d{2}((0[1-9])|(1[0-2]))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$', idcard)
print(y)