# 给你两个整数a和b（-10000<a,b<10000），
# 请你判断是否存在两个整数，他们的和为a，乘积为b。
#
# 若存在，输出Yes,否则输出No
#
# 例如：a=9,b=15,
# 此时不存在两个整数满足上述条件，
# 所以应该输出No。
a=6
b=9
def solve():
    for i in range(1,max(abs(a),abs(b))+1):
        if((b%i==0)&(i+(b//i)==a)):
            # print(i, a - i)
            return "Yes"
    return "No"
print(solve())