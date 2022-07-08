# 堆（优先队列）

# 特征：问题中看到 前 K 大，前 K 小 或者 第 K 个， K 个最 等等类似字样

# 经典题：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # 初始化 k 个数的小根堆，保证每次堆顶就是每次要的结果
        hp = []
        for i, x in enumerate(nums):
            heapq.heappush(hp, x)
            if i >= k:  # 移除比堆顶还要小的数
                heapq.heappop(hp)
        self.hp = hp
        self.k = k
        # print(self.hp)

    def add(self, val: int) -> int:
        heapq.heappush(self.hp, val)
        # 如果添加进来的刚好是第 k 个数
        if self.k < len(self.hp):
            heapq.heappop(self.hp)
        return self.hp[0]
