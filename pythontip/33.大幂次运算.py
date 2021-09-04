# 题目描述：
# 给你两个正整数a(0 < a < 100000)和n(0 <= n <=100000000000)，计算(a^n) % 20132013并输出结果
# 示例：
# 输入：a = 3453 n = 0
#
# 输出：1
a = 3453
n = 2
m=20132013

def mod_again_count(x,y,m):#  模重复平方运算
    a = 1
    b = y#幂
    c = x#基底
    ee = []
   # ib = 0
    while b >= 1:  # 将y转成二进制
        ee.append(b % 2)
        b = b//2
       # ib += 1
    for j in range(0, len(ee)):
        if ee[j] == 1:
            a = (a*c) % m
            c = (c*c) % m
        else:
            c = (c*c) % m
    return a
print(mod_again_count(a,n,m))


# long long fastPower(long long base, long long power) {
#     long long result = 1;
#     while (power > 0) {
#         if (power & 1) {//此处等价于if(power%2==1)
#             result = result * base % 1000;
#         }
#         power >>= 1;//此处等价于power=power/2
#         base = (base * base) % 1000;
#     }
#     return result;
# }
