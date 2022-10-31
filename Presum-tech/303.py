# 303. 区域和检索 - 数组不可变

class NumArray:

    def __init__(self, nums: List[int]):

        
        N=len(nums)

        self.presum=[0]*(N+1)

        for i in range(N):
            self.presum[i+1]=self.presum[i]+nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right+1]-self.presum[left]

