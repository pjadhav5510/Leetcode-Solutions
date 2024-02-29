class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        x = -1
        c = 0

        if len(nums) == 1:
            return 1

        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                c+=1
            else:
                c = 0
            x= max(c,x)
        return x+1
        