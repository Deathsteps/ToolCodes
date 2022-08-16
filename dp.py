# f[n] = max(f[n-1], xxxx)
# => maxValue = max(maxValue, xxxx)

# f[n] = f[n-1] + f[n - 2]
# => a, b = b, a + b

# DP 的时间性能大部分都是 O(N), 空间优化是 O(1)
# DP 矩阵大部分是 O(MN)

# DP 中的状态压缩？其实就是用二进制数来表示动态规划状态转移过程中的状态。
# 什么时候应该状态压缩？
# 状态压缩的题目，一般都会有非常明显的标志：
# 如果你看到有一个参数的数值小于20，同时这道题目中有涉及到是否选取、是否使用这样的二元状态

# https://leetcode.cn/problems/coin-change/solution/yi-pian-wen-zhang-chi-tou-bei-bao-wen-ti-sq9n/
