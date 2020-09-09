# 一个学校，有三间办公室，现在有10位老师，请编写程序，完成随机的分配
import random

nums = [1, 2, 3, [100, 200, 300], 5]

teachers = ['A', 'B', 'C', 'D', 'D', 'F', 'G', 'H', 'I', 'J']
rooms = [[], [], []]
for teacher in teachers:
    room = random.choice(rooms)
    room.append(teacher)
print(rooms)
