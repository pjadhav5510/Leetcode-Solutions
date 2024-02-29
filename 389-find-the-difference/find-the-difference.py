class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        s = Counter(s)
        #t = Counter(t)
        for i in t:
            if i in s and s[i] > 0:
                #t[i] -=1
                s[i] -=1
            else:
                return i

        