class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        i=0
        x=0
        for i in range(len(nums)):
            if nums[i]==target:
                x=i
                print(i)
                break
            elif target < nums[i]:
                x=i
                print(i)
                break
            else:
                x = len(nums)
        return x
            
            