# 题目描述：
# 给你一个整数组成的列表L，按照下列条件输出： 若L是升序排列的,则输出"UP"; 若L是降序排列的,则输出"DOWN"; 若L无序，则输出"WRONG"。
# 示例：
# 输入：L = [1, 1, 3, 3, 4]
#
# 输出：UP
L = [1, 1, 3, 3, 4]
if sorted(L)==L:
    print("UP")
elif L==sorted(L,reverse=1):
    print("DOWN")
else:
    print("WRONG")