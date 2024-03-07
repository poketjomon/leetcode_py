# 题目描述：
# 给你一个整数列表L,判断L中是否存在相同的数字， 若存在，输出YES，否则输出NO。
# 示例：
# 输入：L = [123, 432, 23]
#
# 输出：NO
L = [123, 432, 23]
# def inL(a):
#     for i in range(0,len(a)):
#         for j in range(i,len(a)):
#             if (L[i]==L[j])&(i!=j):
#                 return "YES"
#     return "NO"
# print(inL(L))
print('NO') if len(L) == len(set(L)) else print('YES')