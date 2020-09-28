# 概念：不动用原本的代码，重新定义函数来实现新功能
# 高级装饰器：在装饰器函数里传参数

# 1.定义装饰器函数，高级装饰器函数会有多层函数调用
def can_play(clock):
    print('最外层函数被调用了,clock={}'.format(clock))
    # 2.定义一个inner()函数，inner == play_game
    def inner(fn):
        print('inner函数被调用了,实际上等同于play_gmae被执行了')
        # 3.定义foo函数，相当于给play_game加了条件用于判断，并生成不同的执行结果
        def foo(name, game):
            if clock > 22:
                print('时间太晚了，不能玩游戏了')
            else:
                fn(name, game)
        # 用于返回判断结果
        return foo
    # 用于返回play_game函数
    return inner


# 需求：使用装饰器函数给play_gmae这个方法加一个时间限制
@can_play(23) # 调用can_play这个装饰器函数，并把参数传给clock
def play_game(name, game):
    print('{}正在玩{}'.format(name, game))

play_game('张三','王者荣耀')

'''
1.调用can_play这个装饰器函数，并把参数传给clock
2.紧接着can_play调用inner方法，并把play_game函数当作参数传递到fn fn = play_game()
3.些时foo()等同于play_game('张三','王者荣耀')，并加了判断条件语句，用于输出不同的结果
'''