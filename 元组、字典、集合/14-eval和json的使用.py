# python里有一个比较强大的内置函数eval，可以执行字符串的代码
a = 'input("请输入你的姓名")'
print(a)
# eval(a)  # eval内置函数

# JSON的使用，把列表、元组、字典等转换成JSON字符串
# 字典如果想要把它传给前端页面或者写入到一个文件，需要使用JSON内置函数

import json  # 调用json模块

# dumps将字典、元组、列表等数据转换成JSON字符串,括号内的字符串必须使用双引号
person = {'name': 'zhangsan', 'age': 18, 'gender': 'female'}
m = json.dumps(person)
print(m)
print(type(m))

# loads可以将JSON字符串转换成python里的数据
n = '{"name":"lisi","age":20,"gender":"male"}'
s = json.loads(n)
print(s)
print(type(s))
