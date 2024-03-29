# 题目描述：
# 有一组砝码，重量互不相等，分别为m1、m2、m3……mn；
# 它们可取的最大数量分别为x1、x2、x3……xn。
# 现要用这些砝码去称物体的重量,问能称出多少种不同的重量。
# 现在给你两个正整数列表w和n，
# 列表w中的第i个元素w[i]表示第i个砝码的重量，
# 列表n的第 i个元素n[i]表示砝码i的最大数量。
# i从0开始，请你输出不同重量的种数。
# 如：w=[1,2], n=[2,1], 则输出5（分析：共有五种重量：0,1,2,3,4）
# 示例：
# 输入：w = [1, 2] n = [2, 1]
#
# 输出：5
w = [1, 2]
n = [2, 1]
# s=set()
# b=set()
# s.add(0)
# b.add(0)
# for i in range(0,len(w)):
#     for j in range(0,n[i]+1):
#         s.add(w[i]*n[j])
#
# print(s)
# print(len(s))

W = {0}
L = {0}
for i,v in enumerate(n):
    for j in range(v+1):
        L.add(j * w[i])
    W = {x+y for x in W for y in L}
    L = {0}
print (len(W))