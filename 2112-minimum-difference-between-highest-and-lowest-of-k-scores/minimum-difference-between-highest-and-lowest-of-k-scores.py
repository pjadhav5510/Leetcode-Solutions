class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        #nums = nums.sort()
        print(len(nums))
        if len(nums) == 1:
            return 0
        
        nums.sort()
        i,j = k-1,0
        x=999999
        while i < len(nums):
            x = min(x,nums[i]-nums[j])
            i+=1
            j+=1
        return x