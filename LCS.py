# LCS
# https://zhuanlan.zhihu.com/p/107756084

# 最长公共子串
# https://img-blog.csdnimg.cn/20190324102413405.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NpbmF0XzQxOTE3MTA5,size_16,color_FFFFFF,t_70
# https://img-blog.csdnimg.cn/147453d3b30a4b6caf540aa8f7429d8b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA55CG5oOz5LqM5a-7,size_20,color_FFFFFF,t_70,g_se,x_16


# 最长公共子序列
# https://img-blog.csdnimg.cn/20181120124505151.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDY3MzYwOA==,size_16,color_FFFFFF,t_70
# https://blog.csdn.net/weixin_40673608/article/details/84262695


# 最长公共子序列问题是典型的二维动态规划问题。
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 初始矩阵，多加一行一列方便处理
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    # 最长公共子串的话，只需要在相同的情况里，找到最长的那个串，记录最后的位置和长度
                    # 字符相同，在之前最长基础上 + 1
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:  # 如果是求最长子串，就没有这个 else
                    # 不相同的话，求最长的那个序列。
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        # 整个 dp 矩阵，最后一位就是要求解的值
        return dp[len(text1)][len(text2)]


# 最长回文子串
# https://leetcode.cn/problems/longest-palindromic-substring/submissions/
# 终极解法，Manacher 算法，DP 的时间复杂度是 O(n^2), 而这个方法的复杂度是 O(n)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 初始矩阵，多加一行一列方便处理
        n = len(s)
        if n < 2:
            return s

        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        maxL = 1
        p = 0

        # 回文的填表，只填表的右上部分
        # 枚举子串长度，dp[2L] = dp[1L] && 两头增加的字符是否相等
        for L in range(2, n + 1):
            # 枚举左边界
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > maxL:
                    maxL = j - i + 1
                    p = i

        # print(p, maxL, s[p : p + maxL])
        return s[p : p + maxL]

    def longestPalindrome2(self, s: str) -> str:
        # 初始矩阵，多加一行一列方便处理
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        maxL = 0
        p = 0
        for i in range(n):
            for j in range(n):
                # 回文就是，正串与反串的最长公共子串
                if s[i] == s[n - 1 - j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    if (
                        dp[i + 1][j + 1] > maxL
                        # 这里加个判断筛选掉，abc123cba 这种情况
                        # 首字符位置 + 长度 == 尾字符位置
                        and (n - 1 - j) + (dp[i + 1][j + 1] - 1) == i
                    ):
                        maxL = dp[i + 1][j + 1]
                        p = i

        # print(p, maxL, s[p - maxL + 1 : p + 1])
        return s[p - maxL + 1 : p + 1]


# 最长上升子序列
# https://blog.csdn.net/qq_40507857/article/details/81198662
# LIS 与 LCS
# https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247487814&idx=1&sn=e33023c2d474ff75af83eda1c4d01892


class Solution:
    # 动态规划
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp 表示以 i 为结尾的 LIS 的长度
        dp = [0] * len(nums)
        # 遍历终点填表
        for end in range(len(nums)):
            dp[end] = 1  # 最短也包含一个数
            for start in range(0, end):
                if nums[start] < nums[end]:
                    dp[end] = max(dp[end], dp[start] + 1)
        return max(dp)

    # 贪心 + 二分
    def lengthOfLIS2(self, nums: List[int]) -> int:
        # dp 表示长度为 i+1 的 LIS 结尾元素的最小值
        dp = [nums[0]]  # 第一值没得挑
        # 遍历数组，贪心选值
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                # 二分查找 dp 中第一个大于等于 nums[i] 的并替换
                # 比如 dp: [1, 3, 8] num[i]: 2
                # 2 替换 3 => dp: [1, 2]
                # 这里为什么保留 8:
                # 如果后面 8 没有换掉，则 1、3、8 就是结果
                # 如果 8 换掉了，则 1、2、... 就是结果
                # 这就是 dp[i] 所代表的长度为 i+1 的 LIS 结尾元素的最小值的意思
                dp[self.bs(dp, nums[i])] = nums[i]
            print(dp)

        return len(dp)

    # 求某个条件的二分搜索算法
    def bs(self, arr: List[int], target: int) -> int:
        start = 0
        ret = end = len(arr)
        while start <= end:
            mid = start + ((end - start) >> 1)
            if arr[mid] >= target:
                ret = mid
                end = mid - 1
            else:
                start = mid + 1

        return ret
