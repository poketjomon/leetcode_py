# 题目描述：
# 输入一个日期字符串date_s(格式 %Y-%m-%d), 输出其为星期几？
#
# 备注：星期1 则输出1，星期天 则输出7
#
# 如:
#
# day_weekly('2020-06-06')  -> 5
#
# 想想怎么一行代码搞定，毕竟pythoner 惜字如金！
#
# 示例：
# 输入：date_s = "2020-06-01"
#
# 输出：1
def LeapYear(s):
    if (((s % 4 == 0) & (s % 100 != 0)) | (s % 400 == 0)):
        return 1
    return 0
date_s = "2020-6-5"
data=date_s.split("-")
data_int=[int(i) for i in data]
month={1:31,3:31,5:31,7:31,8:31,10:31,12:31,4:30,6:30,9:30,11:30}
if LeapYear(data_int[0]):
    month.update({2:29})
else:
    month.update({2:28})
Year_sum=0
for i in range(1,data_int[0]):
    if LeapYear(i):
        Year_sum+=366
    else:
        Year_sum+=365
month_sum=0
for j in range(1,data_int[1]):
    month_sum+=month[j]
day_sum=data_int[2]
weekday=(day_sum+Year_sum+month_sum)%7
if(weekday==0):
    weekday=7
print(weekday)




