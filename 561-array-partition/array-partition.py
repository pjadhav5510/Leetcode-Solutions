class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        nums.sort()
        c=0
        for i in range(len(nums)-1,-1,-2):
            c += min(nums[i] ,nums[i-1])
        return c
        