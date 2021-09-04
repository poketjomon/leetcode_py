# 题目描述：
# 回文素数是指一个数既是素数又是回文数。例如，131，既是素数又是回文数。
# 给你一个正整数n(1 <= n <= 100), 请你输出从小到大排列的的第n个回文素数。
#
# 例如：
#
# n = 1, 则输出 2
#
# n = 5, 则输出 11
#
# 示例：
# 输入：n = 1
#
# 输出：2
import math
n = 2
def prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return 0
    return 1
k=2
while n>0:
    if(prime(k))&(str(k)==(str(k)[::-1])):
        n-=1
        k+=1
    else:
        k+=1
print(k-1)


