class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        x = len(nums)
        nums = set(nums)
        b = set()
        for i in range(1,x+1):
            b.add(i)
        
        return list(b-nums)
        