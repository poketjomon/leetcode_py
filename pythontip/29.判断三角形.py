# 题目描述：
# 给你三个整数a,b,c, 判断能否以它们为三个边长构成三角形。 若能，输出YES，否则输出NO。
# 示例：
# 输入：a = 5 b = 5 c = 5
#
# 输出：YES
a = 5
b = 5
c = 5
print("YES"if((a+b>c)&(abs(a-b)<c))else"NO")