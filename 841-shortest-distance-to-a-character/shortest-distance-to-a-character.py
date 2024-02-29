class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:

        a = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == c:
                a.append(i)
        print(a)

        i=0
        j=0
        x=[]
        c = 999999
        for i in range(len(s)):
            for j in range(len(a)):
                c = min(c,abs(i-a[j]))
            x.append(c)
            c = 99999
            
        return x
             