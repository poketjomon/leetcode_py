# 给定两个正整数a和b,
# 利用a / b我们会得到一个长度无限的小数(若a / b不是无限小数，比如1/2=0.5,我们认为0.5是0.5000000...，同样将其看做无限长的小数），
# 小P将该小数点后第x位到第y位的数字当做密码，
# 这样，无论密码有多长，小P只要记住a,b,x,y四个数字就可以了，
# 牢记密码再也不是那么困难的事情了。
# 现在告诉你a,b,x,y（0 < a,b <= 20132013, 0 < x <= y < 100000000000),
# 请你输出密码。
# 例如：a = 1, b = 2, x = 1, y = 4,
# 则 a / b = 0.5000000...,
# 输出小数点后第1到4位数字，即5000
#
# 示例：
# 输入：a = 1 b = 2 x = 1 y = 4
#
# 输出：5000

# round() 取数原则: 4舍6入5留双. 这个算法要要优于4舍5入
a = 1
b = 2
x = 1
y = 4
a=str(round(a/b,y))
a=a.split(".")
print(a)