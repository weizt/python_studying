# 函数就是一段准备好的代码，在需要的时候调用这一段代码即可
# 把多行代码封装成一个整体（函数）
# 在python里，使用关键字def来声明一个函数

# def 函数名（参数）：
#    函数要执行的操作
# 函数定义好了以后并不会自动执行
def tell_story():
    print('从前有座山')
    print('山里有座庙')
    print('庙里有个老和尚')
    print('老和尚在给小和尚讲故事')
    print('故事的内容是：')


age = int(input('请输入你的年龄：'))
if 0 < age < 3:
    for i in range(5):
        tell_story()  # 在需要用的地方调用函数：函数名（参数）
elif 3 <= age < 5:
    tell_story()
else:
    print('滚！')
