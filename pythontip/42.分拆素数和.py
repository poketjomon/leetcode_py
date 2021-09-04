# 题目描述：
# 把一个偶数拆成两个不同素数的和，有几种拆法呢？
# 现在来考虑考虑这个问题，给你一个不超过10000的正的偶数n，
# 计算将该数拆成两个不同的素数之和的方法数，并输出。
# 如n=10，可以拆成3+7，
# 只有这一种方法，因此输出1.
# 示例：
# 输入：n = 4
# 输出：0
n=20
num=0
import math
def is_sushu(x):
    flag=1
    for j in range(2,int(math.sqrt(x))+1):
        if(x%j==0):
            flag=0
    return flag
for i in range(2,n//2):
    if(is_sushu(i))&(is_sushu(n-i)):
            # print(i,n-i)
            num+=1
print(num)