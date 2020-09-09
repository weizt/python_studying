# def function(参数)：
#   函数体
# 调用函数：function(参数)

# 函数声明时，括号里的参数称之为形式参数，简称形参
# 形参的值是不确定的，只是用来占位的
def tell_story(place, person1, person2):
    print('从前有座山')
    print('山里有座' + place)
    print(place + '里有个' + person1)
    print(person1 + '在给' + person2 + '讲故事')
    print('故事的内容是：')


# 调用函数时，传递参数
# 函数调用时传入的参数，才是真正参与运算的数据，称之为实参
# 会把实参一一对的应的传递，交给形参处理
tell_story('怡红院', '头牌', '张三')

# 函数调用时，参数的另一种表达方法
# 直接以定义变量名的形式传递参数，可以改变顺序
tell_story(place='道观', person1='小张', person2='老张')
