class Solution:
    def diStringMatch(self, s: str) -> List[int]:

        b = []
        c = 0
        d = len(s)
        for i in range(len(s)):
            if s[i] == 'I':
                b.append(c)
                c+=1
            elif s[i] == 'D':
                b.append(d)
                d -=1
            
        if s[-1] == 'I':
            b.append(b[-1]+1)
        else:
            b.append(b[-1]-1)
        
        return b


        