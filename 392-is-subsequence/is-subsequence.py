class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i,j,c = 0,0,0
        t = list(t)
        s = list(s)

        while i < len(t) and j < len(s):
            if s == []:
                return True
            if s[j] == t[i]:
                j +=1
                i+=1
                c+=1
            else:
                i +=1
        if c == len(s):
            return True
        else:
            return False