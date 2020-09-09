# 递归简单来说，就是函数内部自己调用自己
# 递归最重要的就是找到出口（停止的条件）
count = 0


def tell_story():
    global count
    count += 1
    print('从前有座山')
    print('山里有座庙')
    print('庙里有个老和尚')
    print('老和尚在给小和尚讲故事')
    print('故事的内容是：')
    if count < 5:
        tell_story()


tell_story()


# 求1~n的和
def get_sum(n):
    if n == 0:
        return 0
    return n + get_sum(n - 1)


print(get_sum(3))
