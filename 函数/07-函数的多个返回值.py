# return语句表示一个函数的结束
def test(a, b):
    x = a // b
    y = a % b
    return x, y
    # return [x,y]
    # return {'x':x,'y':y}


# 一般情况下，一个函数最多只会执行一个return语句
# 特殊情况（finally语句）下，一个函数可能会执行多个return语句

result = test(13, 5)
print('商是{}，余数是{}'.format(result[0], result[1]))
# print('商是{}，余数是{}'.format(result['x'], result['y']))

# 也可以对参数进行拆包
shang, yushu = test(16, 3)
print('商是{}，余数是{}'.format(shang, yushu))
