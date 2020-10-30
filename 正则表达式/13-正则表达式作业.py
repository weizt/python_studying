import re

'''
作业1：用户名匹配
1.用户名只能包含数字、字母和下划线
2.不能以数字开头
3.长度在6到16位范围内
'''

# username = input('请输入用户名：')
# m = re.fullmatch(r'[a-zA-Z_][a-zA-Z0-9_\w]{5,15}', username)
# if m is None:
#     print('用户名不存在')
# else:
#     print(m)

'''
作业2：密码匹配
1.不能包含!@%^&*()字符 
2.必须以字母开头
3.长度在6到13位范围内
'''
# password = input('请输入密码：')
# m1 = re.fullmatch(r'[a-zA-Z][^!@%^&*()]{5,12}', password)
# if m1 is None:
#     print('密码不存在')
# else:
#     print(m1)

'''
作业3：查找文件中符合要求的字符
1.以mobiletrain开头的字符
2.保存在一个列表中
'''

try:
    with open('demo_1.txt', 'r', encoding='utf8') as file:
        content = file.read()
        result = re.findall(r'mobiletrain.*', content)
except FileNotFoundError:
    print('文件未找到')
# result 结果 value 值
print(result)

list = []
try:
    with open('demo_1.txt', 'r', encoding='utf8') as file:
        while True:
            content = file.readline().strip('\n')  # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
            if not content:
                break
            if re.match(r'1000phone.*', content):
                list.append(content)
except FileNotFoundError:
    print('文件未找到')
print(list)

'''
作业4：检测IP地址
1.范围0.0.0.0~255.255.255.255
'''
IP = input('请输入一个数字：')
# \d：表示一位数    [1-9]\d：表示两位数   1[0-9]{2}：表示三位数      2[0-4]\d：表示200-249     25[0-5])：表示250-255
x = re.fullmatch(r'((\d|[1-9]\d|1[0-9]{2}|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1[0-9]{2}|2[0-4]\d|25[0-5])', IP)
print(x)
