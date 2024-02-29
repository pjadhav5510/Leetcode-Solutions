class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        b = []
        
        for i in nums:
            while b and b[-1]>0>i:
                if b[-1] < abs(i):
                    b.pop()
                    continue
                elif b[-1] == abs(i):
                    b.pop()
                break
            else:
                b.append(i)
        return b