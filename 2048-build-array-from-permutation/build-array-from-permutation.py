class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        b=[]

        for i in range(len(nums)):
            x = nums[i]
            b.append(nums[x])
        
        return b