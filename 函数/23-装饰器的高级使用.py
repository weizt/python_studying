# 需求：在20点之前可以玩，20点之后不能玩
# 先搭一个装饰器框架

def can_play(fn):
    def inner(name, game, *args, **kwargs):  # 可以传入可变参数，还可以传入可变关键字参数
        clock = kwargs.get('clock', 23)  # 为防止用户不传入clock关键字参数，使用get方法给定一个默认值
        # clock = args[0]
        if clock < 20:
            fn(name, game)
        else:
            print('时间太晚了不能玩了')

    return inner


@can_play
def game(name, game):
    print('{}正在玩{}'.format(name, game))


game('张三', '王者荣耀')
game('李四', '绝地求生', clock1=18)

# 装饰器的模型
def auth(func):
    def inner(*args, **kwargs):
        # 固定套路，在装饰的函数前做什么
        func(*args, **kwargs)
    return inner


@auth  # 相当于login = auth(login)
def login():
    pass


@auth  # 相当于shopping = auth(shopping)
def shopping():
    pass


@auth  # 相当于pay = auth(pay)
def pay(money, time):
    total_money = money + 1
    pay_time = time
    print(total_money, pay_time)