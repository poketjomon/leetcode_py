# 题目描述：
# 给以一个三角形的三边长a,b和c(边长是浮点数),请你判断三角形的形状。
# 若是锐角三角形，输出R,
# 若是直角三角形，输出Z，
# 若是钝角三角形，输出D，
# 若三边长不能构成三角形，输出W.
# 示例：
# 输入：a = 3.0 b = 5.0 c = 4.0
#
# 输出：Z
a = 4.0
b = 5.0
c = 4.0
def max(x,y,z):
    if(x>y):
        x,y=y,x
    if(y>z):
        y,z=z,y
    return x, y,z
def istrangle(x,y,z):
    if not ((x+y>z)&(abs(x-y)<z)):
        return "W"
    else:
        m=a*a+b*b-c*c
        if(m==0):
            return "Z"
        elif(m>0):
            return "R"
        else:
            return "D"
a,b,c=max(a,b,c)
print(istrangle(a,b,c))