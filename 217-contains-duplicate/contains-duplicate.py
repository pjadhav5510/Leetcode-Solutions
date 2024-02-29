class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = Counter(nums)
        
        print(len(x),len(nums))
        if len(x) != len(nums):    
            return True
        else:
            return False
        