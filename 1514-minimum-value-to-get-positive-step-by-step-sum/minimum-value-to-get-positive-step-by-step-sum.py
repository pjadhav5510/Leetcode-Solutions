class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        
        print(nums)

        temp = min(nums)
        if temp > 0:
            return 1
        else:
            return abs(temp)+1
            
        