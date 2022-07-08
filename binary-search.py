# 输入是已排序的，再使用二分查找

# 二分的判断有很多种情况，最大的变化点在 == target 上做文章

# 二分搜索实际上可以看成在一棵二叉树上搜索
# 时间性能大部分都是 O(logN)

# 有的时间，固定一个数，另一个数用二分查找

# https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/

class Solution:
    # 二分搜索, O(nlogN)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, x in enumerate(nums):
            y = target - x
            i, j = idx + 1, len(nums)
            # 如果 j = len, 则 while i < j and j = mid
            # 如果 j = len-1 , 则 while i <= j and j = mid - 1
            while i < j:
                # i + j 可能会有越界问题，所以这里最好每次都用这种减法的方式求 mid
                # mid = i + ((j - i) >> 1)
                mid = (i + j) // 2

                if nums[mid] == y:
                    return [x, nums[mid]]
                elif nums[mid] < y:
                    i = mid + 1
                else:
                    j = mid

        return []
