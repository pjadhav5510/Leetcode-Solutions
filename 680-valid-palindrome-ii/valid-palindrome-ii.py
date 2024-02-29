class Solution:
    def validPalindrome(self, s: str) -> bool:

        s = list(s)
        i,j = 0,len(s)-1
        c,x=0,0
        while i < j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                c+=1
                j-=1
        
        i,j = 0,len(s)-1
        while i < j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                x+=1
                i+=1

        print(c,x)
        if c < 2 or x<2:
            return True
        else:
            return False

            