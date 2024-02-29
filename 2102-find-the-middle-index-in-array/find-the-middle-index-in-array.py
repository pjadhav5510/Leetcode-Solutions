class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sumL,sumR=0,sum(nums)
        for i in range(len(nums)):
            if sumL==sumR-nums[i]:return i
            sumL+=nums[i]
            sumR-=nums[i]
        return -1