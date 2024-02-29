class Solution:
    def generate(self, nums: int) -> List[List[int]]:
        
        b = []
        b.append([1])
        if nums==1:
            return b
        b.append([1,1])
        if nums == 2:
            return b

        for i in range(3,nums+1):
            b.append([0]*i)    
        print(b)
        for i in range(2,nums):
            for j in range(i):
                b[i][0] = 1
                b[i][-1] = 1
                if j !=0 or j != i:
                    b[i][j] = b[i-1][j-1] + b[i-1][j]
        return b