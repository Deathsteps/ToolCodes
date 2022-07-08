# 单调栈
# 特征：Next Greater Number

# https://leetcode-cn.com/problems/next-greater-element-i/solution/dan-diao-zhan-jie-jue-next-greater-number-yi-lei-w/

# FIXME: 我不理解的是，解题模板里为什么要一定要倒序遍历 nums2
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 对 nums2 中的每一个元素计算它的下一个更大元素
        nextMaxDic = {}
        # 单调递增栈, 栈头永远是最小值
        numStack = []
        for i, x in enumerate(nums2):
            while numStack and x > numStack[-1]:
                nextMaxDic[numStack[-1]] = x
                numStack.pop()
            numStack.append(x)

        # 按 nums1 的要求返回结果
        return list(map(lambda x: nextMaxDic.get(x, -1), nums1))
