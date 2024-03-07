# 题目描述：
# 反素数(逆向拼写的素数)是指一个将其逆向拼写后也是一个素数的非回文数。例如：17和71都是素数，所以，17和71都是反素数。
#
# 给你一个正整数n(1 <= n <= 100), 请你输出从小到大排列的的第n个反素数。
#
# 例如：
#
# n = 1, 则输出 13
#
# n = 5, 则输出 71
#
#
# 示例：
# 输入：n = 1
#
# 输出：13
import math
def IsPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return 0
    return 1
def DianDao(y):
    y=str(y)
    if(y==y[::-1]):
        return 0
    else:
        return int(y[::-1])
n = 5
k=n
prime=13
l=[]
while k>0:
    if IsPrime(prime)&DianDao(prime)&IsPrime(DianDao(prime)):
        k-=1
        l.append(prime)
        prime+=2
    else:
        prime+=2
    # print(prime)
print(l[n-1])

---------------三行--------------------------------
L = [a for a in range(12,1000) if 0 not in [a%b for b in range(2,a)]]
listb = [a for a in L if int(str(a)[::-1]) in L and str(a) != str(a)[::-1]]
print(listb[n-1])