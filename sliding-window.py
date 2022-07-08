# 滑动窗口题

# 特征：
# 该问题的数据结构是数组/字符串类型，且是可迭代的。
# 该问题要求解出该数组/字符串的某个最长/最短子序列（连续的），或某个目标值。

# 关键点：用哪种数据结构表示窗口，如何向窗口添加新元素，如何缩小窗口，在哪里更新结果，窗口的限制条件是什么，debug技巧。
# 维护窗口滑动的单调性

# 一般优化后的复杂度都是 O(N) 即遍历一次数组

# 滑动窗口模板
class Solution:
    def problemName(self, s: str) -> int:
        # Step 1: 定义需要维护的变量们 (对于滑动窗口类题目，这些变量通常是最小长度，最大长度，或者哈希表)
        x, y = ..., ...

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(s)):
            # Step 3: 更新需要维护的变量, 有的变量需要一个if语句来维护 (比如最大最小长度)
            x = new_x
            if condition:
                y = new_y

            '''
            ------------- 下面是两种情况，读者请根据题意二选1 -------------
            '''
            # Step 4 - 情况1
            # 如果题目的窗口长度固定：用一个if语句判断一下当前窗口长度是否达到了限定长度
            # 如果达到了，窗口左指针前移一个单位，从而保证下一次右指针右移时，窗口长度保持不变,
            # 左指针移动之前, 先更新Step 1定义的(部分或所有)维护变量
            if 窗口长度达到了限定长度:
                # 更新 (部分或所有) 维护变量
                # 窗口左指针前移一个单位保证下一次右指针右移时窗口长度保持不变

            # Step 4 - 情况2
            # 如果题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            # 如果当前窗口不合法时, 用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            # 在左指针移动之前更新Step 1定义的(部分或所有)维护变量
            while 不合法:
                # 更新 (部分或所有) 维护变量
                # 不断移动窗口左指针直到窗口再次合法

        # Step 5: 返回答案
        return 123

# Sample2 两变量的滑动窗口
# https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/

# Sample
# https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 1:
            return 1

        # 定义要维护的变量, 最大绝对差
        # 用 python SortedList，或者这里直观点用两个单调队列
        minQ, maxQ = deque(), deque()

        # 返回结果
        ret = 0

        # 定义窗口并滑动
        start = 0
        for end in range(len(nums)):
            # 更新需要维护的变量

            # 保持单调性
            # minQ 维护，窗口内最小值的进入次序, 最后要出队列的值，必需比前面进入的都大
            # 1 2 3 4 5
            while minQ and minQ[-1] > nums[end]:
                minQ.pop()
            # maxQ 维护，窗口内最大值的进入次序，最后要出队列的值，必需比前面进入的都小
            # 9 8 7 6
            while maxQ and maxQ[-1] < nums[end]:
                maxQ.pop()

            # 当前的值即最后用于计算的两个值
            minQ.append(nums[end])
            maxQ.append(nums[end])

            # 窗口可变
            # 合法性判断
            while maxQ and minQ and maxQ[0] - minQ[0] > limit:
                # 先进后出，把最左边的值出站
                if nums[start] == minQ[0]:
                    minQ.popleft()
                if nums[start] == maxQ[0]:
                    maxQ.popleft()
                start += 1

            ret = max(ret, end - start + 1)

        return ret
