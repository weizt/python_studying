# calendar日历模块
import calendar

c = calendar.calendar(2020)
print(c)

# calendar模块用法
calendar.calendar(year, w=2, l=1, c=6)
# 返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
calendar.firstweekday()
# 返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
calendar.isleap(year)
# 是闰年返回True，否则为false。
calendar.leapdays(y1, y2)
# 返回在Y1，Y2两年之间的闰年总数。
calendar.month(year, month, w=2, l=1)
# 返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
calendar.monthcalendar(year, month)
# 返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
calendar.monthrange(year, month)
# 返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
calendar.prcal(year, w=2, l=1, c=6)
# 相当于 print calendar.calendar(year,w,l,c).
calendar.prmonth(year, month, w=2, l=1)
# 相当于 print calendar.calendar（year，w，l，c）。
calendar.setfirstweekday(weekday)
# 设置每周的起始日期码。0（星期一）到6（星期日）。
calendar.timegm(tupletime)
# 和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。
calendar.weekday(year, month, day)
# 返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）
