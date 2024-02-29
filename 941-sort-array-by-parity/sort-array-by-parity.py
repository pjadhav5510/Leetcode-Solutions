class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        b=[]
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                b.append(nums[i])
        
        for i in range(len(nums)):
            if nums[i]%2 != 0:
                b.append(nums[i])

        return b