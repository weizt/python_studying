import re

# 在python中的正则表达式，默认都是贪婪模式，尽可能多的匹配
# 在贪婪模式后面添加 ? 可以将贪婪模式转换成非贪婪模式

m = re.search(r'm.*a', 'mdal5466safssa')
print(m.group())  # ==> mdal5466safssa

# 加 ? 后，尽可能少的匹配
m2 = re.search(r'm.*?a', 'mdal5466safssa')
print(m2.group())  # ==>mda

m3 = re.match(r'aa(\d+?)ddd', 'aa2345ddd')
print(m3.group(0))  # ==> aa2345ddd  必须满足条件，被迫贪婪
print(m3.group(1))  # ==> 2345

m4 = re.match(r'aa(\d+?).*', 'aa2345ddd')
print(m4.group(0))  # ==> aa2345ddd  必须满足条件，被迫贪婪
print(m4.group(1))  # ==> 2  '345ddd' 满足 .*

m5 = re.match(r'aa(\d??)(.*)', 'aa2345ddd')
print(m5.group(0))  # ==> aa2345ddd  必须满足条件，被迫贪婪
print(m5.group(1))  # ==> 空  第一个？表示出现0次或一次，第二个？表示贪婪模式
print(m5.group(2))  # ==> 2345ddd
