class Solution:
    def removeStars(self, s: str) -> str:

        b = []

        for i in s:
            if i == '*':
                b.pop()
            else:
                b+=i

        return ''.join(b)
        
        