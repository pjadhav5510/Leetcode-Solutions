class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        a = []
        i,j=0,0
        x,h=0,-9999
        print(len(nums))
        while j < len(nums):
            a.append(nums[j])
            x+=nums[j]
            if len(a) == k:
                l = x / k
                h = max(l,h)
                print(l)
                x -= a[i]
                a.pop(i)
            j+=1
            
        return h