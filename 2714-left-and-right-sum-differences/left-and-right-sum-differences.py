class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        a,b = [0],[0]
        x=0
        for i in range(len(nums)-1):
            x += nums[i]
            a.append(x)
        print(a)
        x=0
        for i in range(len(nums)-1,0,-1):
            x += nums[i]
            b.append(x)
        print(b)
        b.reverse()

        res=[]
        for i in range(len(a)):
            res.append(abs(a[i] - b[i]))
        return res

        