class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        x = len(nums)
        b = sum(nums)
        lsum = 0
        
        for i in range(x):
            b -= nums[i]
            if b == lsum:
                return i
            lsum += nums[i]
        
        return -1




                