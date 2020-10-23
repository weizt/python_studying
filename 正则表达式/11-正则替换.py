# 正则表达式的作用是用来对字符串进行检索和替换
# 检索方法：match search fullmatch finditer findall
# 替换方法：sub
import re

var1 = 'dslak4444fjl555sd6a'
m1 = re.sub(r'\d', 'x', var1)
print(m1)  # ==> dslakxxxxfjlxxxsdxa

# re.sub()方法的参数:
#    第一个参数：正则表达式
#    第二个参数：新字符或者一个函数
#    第三个参数：需要被替换的原字符串
var2 = 'hello34world78'  # 把字符串中的数字*2


def test(x):
    print(x)
    # < re.Match object;span = (5, 6), match = '3' >
    # < re.Match object;span = (6, 7), match = '4' >
    # < re.Match object;span = (12, 13), match = '7' >
    # < re.Match object;span = (13, 14), match = '8' >
    y = int(x.group(0))
    y *= 2
    return str(y)


# sub()方法自动调用函数，并且给函数传递一个参数，这个参数为re.match类型的对象
m2 = re.sub(r'\d+', test, var2)
print(m2)
