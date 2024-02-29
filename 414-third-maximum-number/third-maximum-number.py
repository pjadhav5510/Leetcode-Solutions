class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        j=0
        b=[]
        c=0

        nums = set(nums)
        nums = list(nums)
        nums.sort()
        print(nums)
        if len(nums) < 3:
            c = max(nums)
            return c
        else:
            return nums[-3]
        #return b[-3]
        


            



            