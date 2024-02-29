class Solution:
    def maxDepth(self, s: str) -> int:

        s=list(s)
        c=0
        j=0
        for i in range(len(s)):
            if s[i] == '(':
                c+=1
                j = max(j,c)
            elif s[i] == ')':
                c -=1
            
        return j


            