class Solution:
    def findLHS(self, nums: List[int]) -> int:
   
        #nums.sort()
        x = Counter(nums)
        a = set(nums)
        
        c = -1
        a=list(a)
        a.sort()
        print(a)
        for i in range(len(a)-1):
            if a[i+1] - a[i] == 1:
                c = max(c, x[a[i+1]] + x[a[i]])
            
        if c == -1:
            return 0
        else:
            return c

            
            