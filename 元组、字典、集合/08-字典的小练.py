chars = ['a', 'c', 'x', 'd', 'p', 'a', 'p', 'a', 'c']
char_count = {}
for char in chars:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)

chars = ['a', 'c', 'x', 'd', 'p', 'a', 'p', 'a', 'c']
char_count = {}
for char in chars:
    if char not in char_count:
        char_count[char] = chars.count(char)
print(char_count)

# 可以使用内置函数max取最大数
vs = char_count.values()
max_count = max(vs)
for k, v in char_count.items():
    if v == max_count:
        print(k)
