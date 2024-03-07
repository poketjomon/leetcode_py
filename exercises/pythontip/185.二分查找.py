# 题目描述：
# 输入一个有序数组nums(int类型, 从小到大排序) 及数字n，输出n在nums 的下标(从0计算)，如果不存在输出-1.
#
# 如:
#
# binary_search([1,2,3],1)  -> 0
#
# binary_search([1,2,3],4)  -> -1
#
# 想想怎么一行代码搞定，毕竟pythoner 惜字如金！
#
# 示例：
# 输入：nums = [1, 1, 2, 3, 4, 5] n = 1
#
# 输出：0
nums = [1, 1, 2, 3, 4, 5]
n = 1
print(nums.index(n) if n in nums else -1)