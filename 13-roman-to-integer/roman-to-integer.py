class Solution:
    def romanToInt(self, s: str) -> int:
        
        k = {'I':1 ,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        x=0
        for i in range(len(s)):
            if i < len(s) - 1 and k[s[i]] < k[s[i+1]]:
                x -= k[s[i]]
            else:
                x += k[s[i]]
        return x