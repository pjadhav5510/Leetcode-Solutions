class Solution:
    def kidsWithCandies(self, c: List[int], extraCandies: int) -> List[bool]:
        b = []
        m = max(c)

        for i in c:
            
            x = i+extraCandies
            print(x,m)
            if x >= m:
                b.append(1)
            else:
                b.append(0)
        return b
        