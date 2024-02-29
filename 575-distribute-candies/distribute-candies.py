class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        x = set(candyType)

        return int(min(len(x),len(candyType)/2))