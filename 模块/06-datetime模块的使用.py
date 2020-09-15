import datetime as dt

# 以一个_开始的 _x
# 以两个__开始的__x
# 以两个__开始，以两个__结束 __x__

# 涉及到四个类 datetime/dae/time/timedelta

# 获取当前的日期时间
print(dt.datetime.now())

# 创建一个日期
print(dt.date(2020, 1, 1))

# 创建一个时间
print(dt.time(18, 23, 45))

# 计算三天后的时间
print(dt.datetime.now() + dt.timedelta(3))
