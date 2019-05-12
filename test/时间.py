import time


# # Sun Apr 28 23:35:24 2019形式
# print(time.asctime(time.localtime(time.time())))
# # 2019-04-28 23:35:24形式
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# # Sun Apr 28 23:35:24 2019格式
# print(time.strftime('%a %b %d %H:%M:%S %Y', time.localtime()))
#
# # 将字符串转化为时间戳
# a = 'Sat Mar 28 22:24:24 2016'
# print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))


# 另一种时间函数
import calendar
# 获取某一个月的日历
cal = calendar.month(2019, 4)
print(cal)