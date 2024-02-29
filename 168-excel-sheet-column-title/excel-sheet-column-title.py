class Solution:
    def convertToTitle(self, n: int) -> str:
        c=n
        m=''
        while c:
            c-=1
            r=c%26
            c//=26
            m=chr(65+r)+m
        return m