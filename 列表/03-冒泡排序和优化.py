nums = [3, 2, 5, 6, 1, 8, 7, 4]
count = 0
j = 0
while j < len(nums) - 1:
    flag = True
    i = 0
    while i < len(nums) - 1 - j:
        count += 1
        if nums[i] > nums[i + 1]:
            flag = False
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        i += 1
    if flag:
        break
    j += 1
    print(nums)
print('比较了%d次' % count)
